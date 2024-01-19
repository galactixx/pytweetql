import json
from typing import List

from api_alchemy.twitter.typing import APIResponse
from api_alchemy.twitter.errors import APIResponseParseError
from api_alchemy.twitter._utils._utils import (
    empty_dictionary,
    extract_dicts_from_list,
    search_key
)

_USER_RESPONSE_KEYS = ['user', 'users']

def validate_response_tweet(response: List[dict]) -> None:
    """
    Validate that the response is tweet data.

    Args:
        response (List[dict]): The response from a Twitter API.
    """
    if empty_dictionary(source=response):
        raise APIResponseParseError('All response fields are empty.')

    objects = search_key(source=response, key='tweet_results')
    if not objects:
        raise APIResponseParseError(
            'This is not a tweet response, please select another parser.'
        )

def validate_response_user(response: List[dict]) -> None:
    """
    Validate that the response is user data.

    Args:
        response (List[dict]): The response from a Twitter API.
    """
    if empty_dictionary(source=response):
        raise APIResponseParseError('All response fields are empty.')

    user_keys = [
        item.get(key) for item in response for key in _USER_RESPONSE_KEYS 
    ]
    if any(user_keys):
        return

    user_objects = search_key(source=response, key='user_results')
    tweet_objects = search_key(source=response, key='tweet_results')
    if not user_objects or (user_objects and tweet_objects):
        raise APIResponseParseError(
            'This is not a user response, please select another parser.'
        )

def validate_response(response: APIResponse) -> APIResponse:
    """
    Validate the response from an API referencing several accepted formats.

    Args:
        response (APIResponse): The response from a Twitter API.

    Returns:
        Tweet: A dataclass consolidating all info from tweet.
    """
    validator = ResponseValidation(response=response)
    if validator.validate_graphql_response():
        return validator.response
    else:
        raise APIResponseParseError('The response is not recognizable.')

class ResponseValidation:
    """
    Functionality to run initial validation on response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        self._response = response

        if self._response is None:
            raise APIResponseParseError('Response is None.')

        if isinstance(self._response, str):
            try:
                if isinstance(self._response, str):
                    self._response = json.loads(self._response)
            except json.JSONDecodeError:
                raise APIResponseParseError(
                    'Response is a string but not in a JSON format.'
                )

        self._response_parsed: dict = None

    @property
    def response(self) -> dict:
        """Return the simply parsed response."""
        return self._response_parsed

    def validate_graphql_response(self) -> bool:
        """
        Validate the response if from GraphQL.

        Args:
            response (dict): The response from the API.

        Returns:
            bool: A boolean indicating whether the response is from GraphQL.
        """
        response = self._response.copy()
        if isinstance(response, dict):
            data_value = response.get('data')
            if data_value is not None:
                self._response_parsed = [data_value]
                return True
        elif isinstance(response, list):
            _response = []
            response_extracted = extract_dicts_from_list(source=response)
            for item in response_extracted:
                data_value = item.get('data')
                if data_value is not None:
                    _response.append(data_value)

            if _response:
                self._response_parsed = _response
                return True

        return False

    def validate_standard_v1_response(self) -> bool:
        """
        """
        pass

    def validate_twitter_v2_response(self) -> bool:
        """
        """
        pass