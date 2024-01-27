from typing import List

from pytweetql.response._base_response import BaseUser
from pytweetql.validation.validation import DirectPathValidation
from pytweetql._utils._data_structures import UserInfo
from pytweetql.validation._base_validation import error_check_output
from pytweetql._typing import Schema

class User(BaseUser):
    """
    Parsing for an individual tweet.
    
    Args:
        user (str): The raw user ID in each user response.
        user_info (dict): The raw user info section in each user response.
    """
    def __init__(self, user: dict, user_info: dict):
        super().__init__(user=user, user_info=user_info)

        self._user = self._parse_user()

    def _parse_user(self) -> UserInfo:
        """
        Parse user info into structured format.

        Returns:
            UserInfo: The dataclass which holds all relevant user detail.
        """
        return UserInfo(
            user_id=self._user_id,
            user_name=self._user_name,
            user_screen_name=self._user_screen_name,
            profile_description=self._profile_description,
            created=self._created_date,
            location=self._location,
            favourites_count=self._favourites_count,
            followers_count=self._followers_count,
            statuses_count=self._statuses_count,
            is_verified=self._is_verified
        )
    
    @property
    def user(self) -> UserInfo:
        """The entire UserInfo dataclass."""
        return self._user
    
    @property
    def user_id(self) -> str:
        """The user ID of the Twitter account."""
        return self._user.user_id
    
    @property
    def user_name(self) -> str:
        """The user name of the Twitter account."""
        return self._user.user_name
        
    @property
    def user_screen_name(self) -> str:
        """The user screen name of the Twitter account."""
        return self._user.user_screen_name
    
    @property
    def profile_description(self) -> str:
        """The user profile description."""
        return self._user.profile_description

    @property
    def created_date(self) -> str:
        """The UTC date the user profile was created."""
        return self._user.created

    @property
    def location(self) -> str:
        """The Location of user."""
        return self._user.location

    @property
    def favourites_count(self) -> int:
        """The number of favorites."""
        return self._user.favourites_count

    @property
    def followers_count(self) -> int:
        """The number of followers."""
        return self._user.followers_count

    @property
    def statuses_count(self) -> int:
        """The number of statuses."""
        return self._user.statuses_count

    @property
    def is_verified(self) -> bool:
        """Boolean indicating whether the user is verified."""
        return self._user.is_verified


class Users(DirectPathValidation):
    """
    Parsing for a user API response.

    Args:
        response (APIResponse): The response from a Twitter API.
        schema (Schema): The schema used to validate the API response.
        endpoint (str): The name the the GraphQL endpoint.
    """
    def __init__(
        self,
        response: List[dict], 
        schema: Schema, 
        endpoint: str
    ):
        super().__init__(response=response)
        self._schema = schema
        self.endpoint = endpoint

        self._users = self._parse_users()

    @property
    def users(self) -> List[User]:
        """Returns all the parsed users."""
        return self._users

    @property
    def num_users(self) -> int:
        """The number of users parsed in response."""
        return len(self._users)

    @error_check_output
    def _parse_users(self) -> List[User]:
        """
        Parse each individual user detail from response.

        Returns:
            List[User]: A list of User classes, one for each user detected.
        """
        return [
            User(**entry) for entry in self.extract_objects(
                schema=self._schema
            )
        ]