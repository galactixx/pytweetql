from typing import List

from omni_parse.twitter.response._base_response import BaseTweet
from omni_parse.twitter._utils._utils import search_key
from omni_parse.twitter.validation._base_validation import BaseStatus
from omni_parse.twitter._utils._data_structures import (
    Status,
    TweetInfo
)

_PROMOTED_TAGS = ['promoted-tweet', 'who-to-follow']

class Tweet(BaseTweet):
    """
    Parsing for an individual tweet.
    
    Args:
        core (dict): The raw core section in each tweet response.
        legacy (dict): The raw legacy section in each tweet response.
        source (dict): The raw source section in each tweet response.
    """
    def __init__(self, core: dict, legacy: dict, source: dict):
        super().__init__(core=core, legacy=legacy, source=source)

        self._tweet = self._parse_tweet()

    def _parse_tweet(self) -> TweetInfo:
        """
        Parse tweet dictionariess into structured format.

        Returns:
            TweetInfo: The dataclass which holds all relevant tweet detail.
        """
        return TweetInfo(
            user_id=self._user_id,
            user_name=self._user_name,
            user_screen_name=self._user_screen_name,
            tweet_id=self._tweet_id,
            created=self._created_date,
            content=self._content,
            language=self._language,
            is_quote=self._is_quote,
            is_retweet=self._is_retweet,
            quote_count=self._quote_count,
            reply_count=self._reply_count,
            retweet_count=self._retweet_count
        )

    @property
    def tweet(self) -> TweetInfo:
        """The entire TweetInfo dataclass."""
        return self._tweet

    @property
    def user_id(self) -> str:
        """The user ID of the Twitter account that posted the tweet."""
        return self._tweet.user_id
    
    @property
    def user_name(self) -> str:
        """The user name of the Twitter account that posted the tweet."""
        return self._tweet.user_name
    
    @property
    def user_screen_name(self) -> str:
        """The user screen name of the Twitter account that posted the tweet."""
        return self._tweet.user_screen_name
    
    @property
    def tweet_id(self) -> str:
        """The tweet ID."""
        return self._tweet.tweet_id
    
    @property
    def created_date(self) -> str:
        """The UTC date the tweet was created."""
        return self._tweet.created
    
    @property
    def content(self) -> str:
        """The text content of the tweet."""
        return self._tweet.content
    
    @property
    def language(self) -> str:
        """The language of the text content."""
        return self._tweet.language
    
    @property
    def quote_count(self) -> int:
        """The number of times the tweet has been quoted."""
        return self._tweet.quote_count
    
    @property
    def reply_count(self) -> int:
        """The number of replies on the tweet."""
        return self._tweet.reply_count
    
    @property
    def retweet_count(self) -> int:
        """The number of times the tweet has been retweeted."""
        return self._tweet.retweet_count
    
    @property
    def is_quote(self) -> bool:
        """Boolean indicating whether it is a quoted tweet."""
        return self._tweet.is_quote
    
    @property
    def is_retweet(self) -> bool:
        """Boolean indicating whether it is a retweet."""
        return self._tweet.is_retweet


class Tweets(BaseStatus):
    """
    Parsing for a tweet-related API response.

    Args:
        response (List[dict]): The response from a Twitter API.
        remove_promotions (bool): Whether to remove promoted tweets from parsing.
        status (Status): The status of the parsing.
    """
    def __init__(
        self,
        response: List[dict],
        remove_promotions: bool,
        status: Status
    ):
        super().__init__(status=status)
        self._response = response
        self._remove_promotions = remove_promotions

        if self.status_code == 200:
            self._tweets = self._parse_tweets()
        else:
            self._tweets = []

    @property
    def tweets(self) -> List[Tweet]:
        """Returns all the parsed tweets."""
        return self._tweets

    @property
    def num_tweets(self) -> int:
        """The number of tweets parsed in response."""
        return len(self._tweets)
    
    def _parse_tweets(self) -> List[Tweet]:
        """
        Parse each individual tweet detail from response and load into list.

        Returns:
            List[Tweet]: A list of Tweet classes, one for each tweet detected.
        """
        parsed_tweets = []

        for entry in self._response:
            entry_result = search_key(source=entry, key='result')
            if entry_result:
                entry_result = entry_result[0]
                core = entry_result.get('core')
                legacy = entry_result.get('legacy')
                source = entry_result.get('source')

                if isinstance(core, dict) and isinstance(legacy, dict):
                    if self._remove_promotions:
                        entry_id = entry.get('entryId')
                        if isinstance(entry_id, str) and any(
                            entry_id.startswith(prom) for prom in _PROMOTED_TAGS
                        ):
                            continue

                    parsed_tweets.append(
                        Tweet(
                            core=core,
                            legacy=legacy,
                            source=source
                        )
                    )

        return parsed_tweets