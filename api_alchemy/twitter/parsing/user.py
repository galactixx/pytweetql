from typing import List

from api_alchemy.twitter.typing import APIResponse
from api_alchemy.twitter.parsing._base_user import BaseUser
from api_alchemy.twitter._utils._utils import search_key
from api_alchemy.twitter._utils._validation import (
    validate_response,
    validate_response_user
)

class User(BaseUser):
    """
    Parsing for an individual tweet.
    
    Args:
        result (dict): The raw result section in each user response.
        legacy (dict): The raw legacy section in each user response.
    """
    def __init__(self, result: dict, legacy: dict):
        super().__init__(result=result, legacy=legacy)

class Users:
    """
    Parsing for a user-related API response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        self._response = validate_response(response=response)

        # Validate that it is a user response
        validate_response_user(response=self._response)

        self._users = self._parse_users()

    def _parse_users(self) -> List[User]:
        """
        Parse each individual user detail from response and load into list.

        Returns:
            List[User]: A list of User classes, one for each user detected.
        """
        parsed_users = []

        entries = search_key(source=self._response, key='entries')
        for entry in entries:
            user_result = search_key(source=entry, key='user_results')
            result = search_key(source=user_result, key='result')
            if isinstance(result, dict):
                legacy = result.get('legacy')

                if legacy is not None:
                    parsed_users.append(
                        User(
                            result=result,
                            legacy=legacy
                        )
                    )

        return parsed_users
    
    @property
    def users(self) -> List[User]:
        """Returns all the parsed users."""
        return self._users

    @property
    def num_users(self) -> int:
        """The number of users parsed in response."""
        return len(self._users)