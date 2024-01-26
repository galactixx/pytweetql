import json
from typing import List

from pytweetql.errors import *
from pytweetql._utils._utils import extract_dicts_from_list
from pytweetql._typing import APIResponse

def error_check_output(func) -> None:
    """"""
    def wrapper(self, *args, **kwargs):
        data = func(self, *args, **kwargs)
        if not data and not self.errors:
            self._error(error=ERROR_PARSER)
        return data
    return wrapper


class BaseStatus:
    """
    Base methods and functionality for accessing response status.

    Args:
        status (Status): The current status of the parsing.
    """
    def __init__(self):
        self._status_code = 200
        self._errors: List[Error] = []

    def _error(self, error: Error) -> None:
        """Append error to list of errors."""
        self._errors.append(error)
        if self._status_code == 200:
            self._status_code = 400

    @property
    def errors(self) -> List[Error]:
        """Returns all errors."""
        return self._errors
    
    @property
    def status_code(self) -> str:
        """Return the current status code."""
        return self._status_code


class BaseValidation(BaseStatus):
    """
    Functionality to run validation on response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        super().__init__()
        self._validate_input_type(response=response)

    @property
    def response(self) -> dict:
        """Return the parsed response."""
        return self._response
    
    @response.setter
    def response(self, response: APIResponse) -> None:
        """Set a new parsed response."""
        self._response = response

    def _validate_input_type(self, response: APIResponse) -> None:
        """
        Validate the response input. Ensure that input is a list or dict. If JSON,
        load and convert.

        Args:
            response (APIResponse): The response from a Twitter API.
        """
        if response is None:
            self._error(error=ERROR_NONE)

        if isinstance(response, str):
            try:
                response = json.loads(response)
            except json.JSONDecodeError:
                self._error(error=ERROR_JSON)
        if not isinstance(response, (dict, list)):
            self._error(error=ERROR_FORMAT)
        else:
            self.response = response
    
    def _validate_response(self) -> None:
        """Validate and ensure the response is from GraphQL."""
        response = self.response.copy()
        
        # If response is a dictionary, convert to list for easy manipulation
        if isinstance(response, dict):
            response = [response]

        if isinstance(response, list):
            _response = []
            response_extracted = extract_dicts_from_list(source=response)

            for item in response_extracted:
                data_value = item.get('data')
                if isinstance(data_value, dict):
                    _response.append(data_value)

            if _response:
                self.response = _response
                return
            else:
                self._error(error=ERROR_FORMAT)