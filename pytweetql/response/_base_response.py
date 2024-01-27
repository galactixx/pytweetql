from pytweetql._utils._utils import (
    verify_boolean,
    verify_datetime,
    verify_integer
)

class BaseTweet:
    """
    Raw parsing for an individual tweet.
    
    Args:
        user (dict): The raw user section in each tweet response.
        user_info (dict): The raw user info section in each tweet response.
        tweet (dict): The raw tweet section in each tweet response.
        source (str): The raw source section in each tweet response.
    """
    def __init__(self, user: dict, user_info: dict, tweet: dict, source: str):
        self._user = user
        self._user_info = user_info
        self._tweet = tweet
        self._source = source

    @property
    def _user_id(self) -> str:
        """The user ID of the Twitter account that posted the tweet."""
        return self._user.get('rest_id')

    @property
    def _user_name(self) -> str:
        """The user name of the Twitter account that posted the tweet."""
        return self._user_info.get('name')
        
    @property
    def _user_screen_name(self) -> str:
        """The user screen name of the Twitter account that posted the tweet."""
        return self._user_info.get('screen_name')

    @property
    def _tweet_id(self) -> str:
        """The tweet ID."""
        return self._tweet.get('id_str')

    @property
    def _created_date(self) -> str:
        """The UTC date the tweet was created."""
        return verify_datetime(created=self._tweet.get('created_at'))
        
    @property
    def _content(self) -> str:
        """The text content of the tweet."""
        return self._tweet.get('full_text')

    @property
    def _language(self) -> str:
        """The language of the text content."""
        return self._tweet.get('lang')
    
    @property
    def _quote_count(self) -> int:
        """The number of times the tweet has been quoted."""
        return verify_integer(integer=self._tweet.get('quote_count'))
        
    @property
    def _reply_count(self) -> int:
        """The number of replies on the tweet."""
        return verify_integer(integer=self._tweet.get('reply_count'))
        
    @property
    def _retweet_count(self) -> int:
        """The number of times the tweet has been retweeted."""
        return verify_integer(integer=self._tweet.get('retweet_count'))
        
    @property
    def _is_quote(self) -> bool:
        """Boolean indicating whether it is a quoted tweet."""
        return verify_boolean(boolean=self._tweet.get('is_quote_status'))
        
    @property
    def _is_retweet(self) -> bool:
        """Boolean indicating whether it is a retweet."""
        return verify_boolean(boolean=self._tweet.get('retweeted'))


class BaseUser:
    """
    Raw parsing for an individual user.

    Args:
        user (str): The raw user ID in each user response.
        user_info (dict): The raw user info section in each user response.
    """
    def __init__(self, user: str, user_info: dict):
        self._user = user
        self._user_info = user_info

    @property
    def _user_id(self) -> str:
        """The user ID of the Twitter account."""
        return self._user
    
    @property
    def _user_name(self) -> str:
        """The user name of the Twitter account."""
        return self._user_info.get('name')
        
    @property
    def _user_screen_name(self) -> str:
        """The user screen name of the Twitter account."""
        return self._user_info.get('screen_name')
    
    @property
    def _profile_description(self) -> str:
        """The user profile description."""
        return self._user_info.get('description')

    @property
    def _created_date(self) -> str:
        """The UTC date the user profile was created."""
        return verify_datetime(created=self._user_info.get('created_at'))

    @property
    def _location(self) -> str:
        """The Location of user."""
        return self._user_info.get('location')

    @property
    def _favourites_count(self) -> int:
        """The number of favorites."""
        return verify_integer(integer=self._user_info.get('favourites_count'))

    @property
    def _followers_count(self) -> int:
        """The number of followers."""
        return verify_integer(integer=self._user_info.get('followers_count'))

    @property
    def _statuses_count(self) -> int:
        """The number of statuses."""
        return verify_integer(integer=self._user_info.get('statuses_count'))

    @property
    def _is_verified(self) -> bool:
        """Boolean indicating whether the user is verified."""
        return verify_boolean(boolean=self._user_info.get('verified'))