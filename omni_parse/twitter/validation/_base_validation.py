from abc import ABC, abstractmethod
import json
from typing import List

from omni_parse.twitter._utils._data_structures import Status
from omni_parse.twitter.status import *
from omni_parse.twitter.typing import APIResponse

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

class _BaseValidation(ABC):
    """
    Base abstract functionality for validation of response.
    """
    @abstractmethod
    def validate_response_tweet(self, response: List[dict]) -> None:
        """
        Validate that the response is tweet data.
        """
        pass

    @abstractmethod
    def validate_response_user(self, response: List[dict]) -> None:
        """
        Validate that the response is user data.
        """
        pass

    @abstractmethod
    def validate_response() -> None:
        """
        Validate the response.
        """

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

    def _update_status(self, status: Status) -> None:
        """
        Register and track the validation error that occurs.

        Args:
            error (Status): The error.
        """
        self._status = status

    def _initial_validation(self, response: APIResponse) -> APIResponse:
        """
        """
        if response is None:
            self._update_status(status=error_response_none)

        if isinstance(response, str):
            try:
                if isinstance(response, str):
                    return json.loads(response)
            except json.JSONDecodeError:
                self._update_status(status=error_invalid_json)
        return response