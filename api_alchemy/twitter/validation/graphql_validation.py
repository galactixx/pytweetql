from api_alchemy.twitter.errors import *
from api_alchemy.twitter.validation.base_validation import BaseValidation
from api_alchemy.twitter.typing import APIResponse
from api_alchemy.twitter._utils._utils import (
    empty_dictionary,
    extract_dicts_from_list,
    search_key
)

_USER_RESPONSE_KEYS = ['user', 'users']

class GraphQLValidation(BaseValidation):
    """
    Functionality to run validation on response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        super().__init__(response=response)

    def validate_response(self) -> None:
        """
        Validate whether the GraphQL response.
        """
        if self.status == 'success':
            response = self._response.copy()
            if isinstance(response, dict):
                data_value = response.get('data')
                if data_value is not None:
                    self._response = [data_value]
                    return
            elif isinstance(response, list):
                _response = []
                response_extracted = extract_dicts_from_list(source=response)
                for item in response_extracted:
                    data_value = item.get('data')
                    if data_value is not None:
                        _response.append(data_value)

                if _response:
                    self._response = _response
                    return
                
            self._add_error(error=error_format_invalid)
    
    def validate_response_tweet(self) -> None:
        """
        Validate that the response is tweet data.
        """
        if self.status == 'success':
            if empty_dictionary(source=self._response):
                self._add_error(error=error_response_empty)

            objects = search_key(self, source=self._response, key='tweet_results')
            if not objects:
                self._add_error(error=error_invalid_parser)

    def validate_response_user(self) -> None:
        """
        Validate that the response is user data.
        """
        if self.status == 'success':
            if empty_dictionary(source=self._response):
                self._add_error(error=error_response_empty)

            user_keys = [
                item.get(key) for item in self._response
                for key in _USER_RESPONSE_KEYS 
            ]
            if any(user_keys):
                return

            user_objects = search_key(source=self._response, key='user_results')
            tweet_objects = search_key(source=self._response, key='tweet_results')
            if not user_objects or (user_objects and tweet_objects):
                self._add_error(error=error_invalid_parser)