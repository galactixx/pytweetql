from omni_parse.twitter._utils._utils import (
    verify_boolean,
    verify_datetime,
    verify_integer
)

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