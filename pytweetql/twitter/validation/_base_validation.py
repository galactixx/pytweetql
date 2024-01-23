from abc import ABC, abstractmethod
import json
from typing import List

from pytweetql.twitter._utils._data_structures import Status
from pytweetql.twitter.status import *
from pytweetql.twitter.typing import APIResponse

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
    def __init__(self, status: Status):
        self._status = status

    @property
    def status_message(self) -> dict:
        """Return the message associated with the status."""
        return self._status.message
    
    @property
    def status_code(self) -> str:
        """Return the code associated with the status."""
        return self._status.status_code
    
    @property
    def status(self) -> str:
        """Return the current status."""
        return self._status
    
    @status.setter
    def status(self, status: Status) -> None:
        """Set a new status."""
        self._status = status


class _BaseValidation(ABC):
    """
    Base abstract functionality for validation of response.
    """

    @abstractmethod
    def validate_response_list(self, response: List[dict]) -> None:
        """Validate that the response is list data."""
        pass

    @abstractmethod
    def validate_response_tweet(self, response: List[dict]) -> None:
        """Validate that the response is tweet data."""
        pass

    @abstractmethod
    def validate_response_user(self, response: List[dict]) -> None:
        """Validate that the response is user data."""
        pass

    @abstractmethod
    def _validate_response(self) -> None:
        """Initial validation of the response."""
        pass


class BaseValidation(BaseStatus, _BaseValidation):
    """
    Functionality to run validation on response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        super().__init__(status=success_response)
        self._response: List[dict] = self._initial_validation(response=response)

    @property
    def response(self) -> dict:
        """Return the parsed response."""
        return self._response
    
    @response.setter
    def response(self, response: APIResponse) -> None:
        """Set a new parsed response."""
        self._response = response

    def _initial_validation(self, response: APIResponse) -> APIResponse:
        """
        """
        if response is None:
            self.status = error_response_none

        if isinstance(response, str):
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                self.status = error_invalid_json
        if not isinstance(response, (dict, list)):
            self.status = error_format_invalid
        return response