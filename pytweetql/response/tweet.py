from typing import List

from pytweetql.response._base_response import BaseTweet
from pytweetql.validation.validation import DirectPathValidation
from pytweetql._utils._data_structures import TweetInfo
from pytweetql.validation._base_validation import error_check_output
from pytweetql._typing import Schema

class Tweet(BaseTweet):
    """
    Parsing for an individual tweet.
    
    Args:
        user (dict): The raw user section in each tweet response.
        user_info (dict): The raw user info section in each tweet response.
        tweet (dict): The raw tweet section in each tweet response.
        source (str): The raw source section in each tweet response.
    """
    def __init__(
        self, 
        user: dict, 
        user_info: dict, 
        tweet: dict, 
        source: str
    ):
        super().__init__(
            user=user,
            user_info=user_info, 
            tweet=tweet, 
            source=source
        )

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


class Tweets(DirectPathValidation):
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
        schema: Schema,
        remove_promotions: bool,
        endpoint: str
    ):
        super().__init__(response=response)
        self._schema = schema
        self._remove_promotions = remove_promotions
        self.endpoint = endpoint

        self._tweets = self._parse_tweets()

    @property
    def tweets(self) -> List[Tweet]:
        """Returns all the parsed tweets."""
        return self._tweets

    @property
    def num_tweets(self) -> int:
        """The number of tweets parsed in response."""
        return len(self._tweets)
    
    @error_check_output
    def _parse_tweets(self) -> List[Tweet]:
        """
        Parse each individual tweet detail from response and load into list.

        Returns:
            List[Tweet]: A list of Tweet classes, one for each tweet detected.
        """
        return [
            Tweet(**entry) for entry in self.extract_objects(
                schema=self._schema
            )
        ]