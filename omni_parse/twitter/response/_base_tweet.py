from omni_parse.twitter._utils._utils import (
    return_value,
    verify_boolean,
    verify_datetime,
    verify_integer
)

class BaseTweet:
    """
    Parsing from the raw response of an individual tweet.

    Args:
        core (dict): The raw core section in each tweet response.
        legacy (dict): The raw legacy section in each tweet response.
        source (dict): The raw source section in each tweet response.
    """
    def __init__(self, core: dict, legacy: dict, source: dict):
        self._core = core
        self._legacy = legacy
        self._source = source

    @property
    def _user_id(self) -> str:
        """The user ID of the Twitter account that posted the tweet."""
        return return_value(source=self._core, key='rest_id')

    @property
    def _user_name(self) -> str:
        """The user name of the Twitter account that posted the tweet."""
        return return_value(source=self._core, key='name')
        
    @property
    def _user_screen_name(self) -> str:
        """The user screen name of the Twitter account that posted the tweet."""
        return return_value(source=self._core, key='screen_name')

    @property
    def _tweet_id(self) -> str:
        """The tweet ID."""
        return self._legacy.get('id_str')

    @property
    def _created_date(self) -> str:
        """The UTC date the tweet was created."""
        return verify_datetime(created=self._legacy.get('created_at'))
        
    @property
    def _content(self) -> str:
        """The text content of the tweet."""
        return self._legacy.get('full_text')

    @property
    def _language(self) -> str:
        """The language of the text content."""
        return self._legacy.get('lang')
    
    @property
    def _quote_count(self) -> str:
        """The number of times the tweet has been quoted."""
        return verify_integer(integer=self._legacy.get('quote_count'))
        
    @property
    def _reply_count(self) -> str:
        """The number of replies on the tweet."""
        return verify_integer(integer=self._legacy.get('reply_count'))
        
    @property
    def _retweet_count(self) -> str:
        """The number of times the tweet has been retweeted."""
        return verify_integer(integer=self._legacy.get('retweet_count'))
        
    @property
    def _is_quote(self) -> str:
        """Boolean indicating whether it is a quoted tweet."""
        return verify_boolean(boolean=self._legacy.get('is_quote_status'))
        
    @property
    def _is_retweet(self) -> str:
        """Boolean indicating whether it is a retweet."""
        return verify_boolean(boolean=self._legacy.get('retweeted'))
