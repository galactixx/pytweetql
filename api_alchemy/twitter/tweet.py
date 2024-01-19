from typing import List

from api_alchemy.twitter.typing import APIResponse
from api_alchemy.twitter.utils._data_structures import TweetInfo
from api_alchemy.twitter.utils._utils import (
    find_key,
    return_value,
    verify_boolean,
    verify_datetime,
    verify_integer
)
from api_alchemy.twitter.utils._validation import (
    validate_response,
    validate_response_tweet
)

class Tweet:
    """
    Parsing for an individual tweet.
    
    Args:
        core (dict): The raw core section in each tweet response.
        legacy (dict): The raw legacy section in each tweet response.
        source (dict): The raw source section in each tweet response.
    """
    def __init__(self, core: dict, legacy: dict, source: dict):
        self._core = core
        self._legacy = legacy
        self._source = source

        self._tweet = self._parse_tweet()

    def _parse_tweet(self) -> TweetInfo:
        """
        Parse tweet dictionariess into structured format.

        Returns:
            TweetInfo: The dataclass which holds all relevant tweet detail.
        """
        user_id = return_value(obj=self._core, key='rest_id')
        user_name = return_value(obj=self._core, key='name')
        user_screen_name = return_value(obj=self._core, key='screen_name')

        created = verify_datetime(created=self._legacy.get('created_at'))
        quote_count = verify_integer(integer=self._legacy.get('quote_count'))
        reply_count = verify_integer(integer=self._legacy.get('reply_count'))
        retweet_count = verify_integer(integer=self._legacy.get('retweet_count'))
        is_quote = verify_boolean(boolean=self._legacy.get('is_quote_status'))
        is_retweet = verify_boolean(boolean=self._legacy.get('retweeted'))

        return TweetInfo(
            user_id=user_id,
            user_name=user_name,
            user_screen_name=user_screen_name,
            tweet_id=self._legacy.get('id_str'),
            created=created,
            content=self._legacy.get('full_text'),
            language=self._legacy.get('lang'),
            is_quote=is_quote,
            is_retweet=is_retweet,
            quote_count=quote_count,
            reply_count=reply_count,
            retweet_count=retweet_count
        )

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
    def twet_id(self) -> str:
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
    def is_quote(self) -> bool:
        """Boolean indicating whether it is a quoted tweet."""
        return self._tweet.is_quote
    
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

class Tweets:
    """
    Parsing for a tweet-related API response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        self._response = validate_response(response=response)

        # Validate that it is a tweet response
        validate_response_tweet(response=self._response)

        self._tweets = self._parse_tweets()

    def _parse_tweets(self) -> List[Tweet]:
        """
        Parse each individual tweet detail from response and load into list.

        Returns:
            List[Tweet]: A list of tweet classes, one for each tweet detected.
        """
        parsed_tweets = []

        instructions = find_key(obj=self._response, key='instructions')
        entries = find_key(obj=instructions, key='entries')

        nested_list = all(isinstance(entry, list) for entry in entries)
        if nested_list:
            entries = entries[0]

        for entry in entries:
            entry_result = find_key(obj=entry, key='result')
            if entry_result:
                entry_result = entry_result[0]
                core = entry_result.get('core')
                legacy = entry_result.get('legacy')
                source = entry_result.get('source')

                if core is not None and legacy is not None:
                    parsed_tweets.append(
                        Tweet(
                            core=core,
                            legacy=legacy,
                            source=source
                        )
                    )

        return parsed_tweets

    @property
    def tweets(self) -> List[Tweet]:
        """Returns all the parsed tweets."""
        return self._tweets

    @property
    def num_tweets(self) -> int:
        """The number of tweets parsed in response."""
        return len(self._tweets)