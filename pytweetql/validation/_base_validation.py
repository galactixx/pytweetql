import json
from typing import List

from pytweetql.errors import *
from pytweetql._typing import APIResponse
from pytweetql._utils._utils import extract_dicts_from_list
from pytweetql.response.error import Error

def status_code_check(func) -> None:
    def wrapper(self, *args, **kwargs):
        if self.status_code == 200:
            return func(self, *args, **kwargs)
    return wrapper


class BaseStatus:
    """
    Base methods and functionality for accessing response status.

    Args:
        status (Status): The current status of the parsing.
    """
    def __init__(self):
        self._status_code = 200
        self._errors: List[ValidationError] = []

    def _error(self, error: ValidationError) -> None:
        """Append error to list of errors."""
        self._errors.append(error)
        if self._status_code == 200:
            self._status_code = 400
    
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
    
    @status_code_check
    def _validate_response(self) -> None:
        """Validate and ensure the response is from GraphQL."""
        response = self.response.copy()
        
        # If response is a dictionary, convert to list for easy manipulation
        if isinstance(response, dict):
            response = [response]

        if isinstance(response, list):
            _response = []
            response_extracted = extract_dicts_from_list(source=response)

            # # Check if the API response resulted in an error
            # errors = BaseValidation.detect_errors(response=response_extracted)
            # if not response_extracted:
            #     if errors:
            #         for error in errors:
            #             self._error(
            #                 error=generate_api_error(message=error.message)
            #             )
            #     else:
            #         self._error(error=ERROR_API_UNKNOWN)
            #     return

            for item in response_extracted:
                data_value = item.get('data')
                if isinstance(data_value, dict):
                    _response.append(data_value)

            if _response:
                self.response = _response
                return
        self._error(error=ERROR_FORMAT)