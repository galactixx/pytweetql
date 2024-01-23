from pytweetql.twitter._utils._utils import (
    return_value,
    verify_boolean,
    verify_datetime,
    verify_integer
)

class BaseError:
    """
    Parsing from the raw response of an individual error message.

    Args:
        message (dict): The raw error message dictionary.
    """
    def __init__(self, message: dict):
        self._message_error = message

    @property
    def _message(self) -> str:
        """The message which describes the error."""
        return self._message_error.get('message')
    
    @property
    def _code(self) -> int:
        """An integer code associated with the error."""
        return verify_integer(integer=self._message_error.get('code'))


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
    def _quote_count(self) -> int:
        """The number of times the tweet has been quoted."""
        return verify_integer(integer=self._legacy.get('quote_count'))
        
    @property
    def _reply_count(self) -> int:
        """The number of replies on the tweet."""
        return verify_integer(integer=self._legacy.get('reply_count'))
        
    @property
    def _retweet_count(self) -> int:
        """The number of times the tweet has been retweeted."""
        return verify_integer(integer=self._legacy.get('retweet_count'))
        
    @property
    def _is_quote(self) -> bool:
        """Boolean indicating whether it is a quoted tweet."""
        return verify_boolean(boolean=self._legacy.get('is_quote_status'))
        
    @property
    def _is_retweet(self) -> bool:
        """Boolean indicating whether it is a retweet."""
        return verify_boolean(boolean=self._legacy.get('retweeted'))


class BaseUser:
    """
    Parsing from the raw response of an individual user.

    Args:
        result (dict): The raw result section in each user response.
        legacy (dict): The raw legacy section in each user response.
    """
    def __init__(self, result: dict, legacy: dict):
        self._result = result
        self._legacy = legacy

    @property
    def _user_id(self) -> str:
        """The user ID of the Twitter account."""
        return self._result.get('rest_id')
    
    @property
    def _user_name(self) -> str:
        """The user name of the Twitter account."""
        return self._legacy.get('name')
        
    @property
    def _user_screen_name(self) -> str:
        """The user screen name of the Twitter account."""
        return self._legacy.get('screen_name')
    
    @property
    def _profile_description(self) -> str:
        """The user profile description."""
        return self._legacy.get('description')

    @property
    def _created_date(self) -> str:
        """The UTC date the user profile was created."""
        return verify_datetime(created=self._legacy.get('created_at'))

    @property
    def _location(self) -> str:
        """The Location of user."""
        return self._legacy.get('location')

    @property
    def _favourites_count(self) -> int:
        """The number of favorites."""
        return verify_integer(integer=self._legacy.get('favourites_count'))

    @property
    def _followers_count(self) -> int:
        """The number of followers."""
        return verify_integer(integer=self._legacy.get('followers_count'))

    @property
    def _statuses_count(self) -> int:
        """The number of statuses."""
        return verify_integer(integer=self._legacy.get('statuses_count'))

    @property
    def _is_verified(self) -> bool:
        """Boolean indicating whether the user is verified."""
        return verify_boolean(boolean=self._legacy.get('verified'))


class BaseList:
    """
    Parsing from the raw response of an individual list.

    Args:
        entry (dict): The raw data section in each list response.
    """
    def __init__(self, entry: dict):
        self._entry = entry

    @property
    def _name(self) -> str:
        """The list name."""
        return self._entry.get('name')
    
    @property
    def _description(self) -> str:
        """The list description."""
        return self._entry.get('description')
    
    @property
    def _list_id(self) -> str:
        """The list ID."""
        return self._entry.get('id_str')
    
    @property
    def _member_count(self) -> int:
        """The number of members in the list."""
        return verify_integer(integer=self._entry.get('member_count'))

    @property
    def _is_private(self) -> bool:
        """Boolean indicating whether the list is private."""
        return verify_boolean(boolean=self._entry.get('member_count'))
    
    @property
    def _is_following(self) -> bool:
        """Boolean indicating whether the user is following the list."""
        return verify_boolean(boolean=self._entry.get('member_count'))