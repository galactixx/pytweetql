from typing import List

from omni_parse.twitter.status import *
from omni_parse.twitter._utils._data_structures import Status
from omni_parse.twitter.typing import APIResponse
from omni_parse.twitter.validation._base_validation import (
    BaseValidation,
    status_code_check
)
from omni_parse.twitter._utils._utils import (
    empty_dictionary,
    extract_dicts_from_list,
    search_key
)

_LIST_TYPES = ['list']
_USER_TYPES = ['user']
_TWEET_TYPES = ['who-to-follow', 'tweet', 'promoted-tweet']

_LIST_RESULTS = 'list'
_USER_RESULTS = 'user_results'
_TWEET_RESULTS = 'tweet_results'

class GraphQLValidation(BaseValidation):
    """
    Functionality to run validation on response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        super().__init__(response=response)

        self._validate_response()

        if empty_dictionary(source=self.response):
            self.status = error_response_empty

    @status_code_check
    def _search_entries(self, results: str, types: list) -> None:
        """
        Search through entries to confirm type of data retrieved.
        
        Args:
            types (list): A list of expected types as strings.
        """
        entries = search_key(source=self.response, key='entries')
        if entries:
            entry_id: str = entries[0].get('entryId')
            if entry_id is not None:
                entry_type = entry_id.split('-')[0]
                if entry_type not in types:
                    self.status = error_invalid_parser
                else:
                    self.response = entries
        else:
            results = search_key(source=self.response, key=results)
            if results:
                self.response = results
            else:
                self.status = error_format_invalid

    @status_code_check
    def _validate_response(self) -> None:
        """Validate whether the GraphQL response."""
        response = self.response.copy()
        
        # If response is a dictionary, convert to list for easy manipulation
        if isinstance(response, dict):
            response = [response]

        # Check if the API response resulted in an error
        if isinstance(response, list):
            _response = []
            errors = []
            response_extracted = extract_dicts_from_list(source=response)

            for item in response_extracted[:]:
                messages: List[dict] = item.get('errors')
                if messages:
                    response_extracted.remove(item)
                    for error in messages:
                        message = error.get('message')
                        if message:
                            errors.append(message)
            if not response_extracted:
                if errors:
                    errors_messages = '\n'.join(message for message in errors)
                    self.status = Status(
                        status_code=502,
                        message=f'API request error: {errors_messages}'
                    )
                else:
                    self.status = error_api_unknown
                return

            for item in response_extracted:
                data_value = item.get('data')
                if data_value is not None:
                    _response.append(data_value)

            if _response:
                self.response = _response
                return
        self.status = error_format_invalid

    @status_code_check
    def validate_response_list(self) -> None:
        """Validate that the response is list data."""
        self._search_entries(results=_LIST_RESULTS, types=_LIST_TYPES)

    @status_code_check
    def validate_response_tweet(self) -> None:
        """Validate that the response is tweet data."""
        self._search_entries(results=_TWEET_RESULTS, types=_TWEET_TYPES)

    @status_code_check
    def validate_response_user(self) -> None:
        """Validate that the response is user data."""
        self._search_entries(results=_USER_RESULTS, types=_USER_TYPES)