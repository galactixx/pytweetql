from typing import List

from pytweetql.twitter.status import *
from pytweetql.twitter._constants import *
from pytweetql.twitter.typing import APIResponse
from pytweetql.twitter.response.error import (
    Error,
    format_errors
)
from pytweetql.twitter.validation._base_validation import (
    BaseValidation,
    status_code_check
)
from pytweetql.twitter._utils._utils import (
    empty_dictionary,
    extract_dicts_from_list,
    search_key
)

class Validation(BaseValidation):
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

    @staticmethod
    def detect_errors(response: List[dict]) -> List[Error]:
        """
        Detect any API generated errors in response.

        Args:
            response (List[dict]): The semi-parsed API response.

        Returns:
            List[Error]: Any errors found in reponse, each as Error class.
        """
        errors = []
        for item in response[:]:
            messages: List[dict] = item.get('errors')
            if messages:
                response.remove(item)
                for message in messages:
                    error = Error(message=message)
                    if error.message:
                        errors.append(error)
        return errors

    @status_code_check
    def _search_entries(self, keys: list, types: list) -> None:
        """
        Search through entries to confirm type of data retrieved.
        
        Args:
            types (list): A list of expected types as strings.
        """
        entries = search_key(source=self.response, key='entries')
        if entries:
            entry_id = entries[0].get('entryId')
            if isinstance(entry_id, str):
                entry_type = entry_id.split('-')[0]
                if entry_type not in types:
                    self.status = error_invalid_parser
                else:
                    self.response = entries
        else:
            _response = []
            for data in self.response:
                data_keys = list(data.keys())
                if len(data_keys) == 1 and data_keys[0] in keys:
                    _response.append(data.get(data_keys[0]))
            
            self.response = extract_dicts_from_list(source=_response)
            if not self.response:
                self.status = error_invalid_parser

    @status_code_check
    def _validate_response(self) -> None:
        """Validate whether the GraphQL response."""
        response = self.response.copy()
        
        # If response is a dictionary, convert to list for easy manipulation
        if isinstance(response, dict):
            response = [response]

        if isinstance(response, list):
            _response = []
            response_extracted = extract_dicts_from_list(source=response)

            # Check if the API response resulted in an error
            errors = Validation.detect_errors(response=response_extracted)
            if not response_extracted:
                if errors:
                    self.status = format_errors(errors=errors)
                else:
                    self.status = error_api_unknown
                return

            for item in response_extracted:
                data_value = item.get('data')
                if isinstance(data_value, dict):
                    _response.append(data_value)

            if _response:
                self.response = _response
                return
        self.status = error_format_invalid

    @status_code_check
    def validate_response_list(self) -> None:
        """Validate that the response is list data."""
        self._search_entries(keys=LIST_KEYS, types=LIST_TYPES)

    @status_code_check
    def validate_response_tweet(self) -> None:
        """Validate that the response is tweet data."""
        self._search_entries(keys=TWEET_KEYS, types=TWEET_TYPES)

    @status_code_check
    def validate_response_user(self) -> None:
        """Validate that the response is user data."""
        self._search_entries(keys=USER_KEYS, types=USER_TYPES)