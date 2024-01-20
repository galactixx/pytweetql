from abc import ABC, abstractmethod
import json
from typing import List

from omni_parse.twitter._utils._data_structures import ValidationError
from omni_parse.twitter.errors import *
from omni_parse.twitter.typing import (
    APIResponse,
    ParseStatus
)

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

class BaseValidation(_BaseValidation):
    """
    Functionality to run validation on response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        self._error: ValidationError = None
        self._status: ParseStatus = 'success'
        self._response: List[dict] = self._initial_validation(response=response)

    @property
    def error(self) -> dict:
        """Return the error that occurred."""
        return self._error

    @property
    def response(self) -> dict:
        """Return the parsed response."""
        return self._response
    
    @property
    def status(self) -> str:
        """Return the current parse status."""
        return self._status

    def _add_error(self, error: ValidationError) -> None:
        """
        Register and track the validation error that occurs.

        Args:
            error (ValidationError): The error.
        """
        self._status = 'failure'
        self._error = error

    def _initial_validation(self, response: APIResponse) -> APIResponse:
        """
        """
        if response is None:
            self._add_error(error=error_response_none)

        if isinstance(response, str):
            try:
                if isinstance(response, str):
                    return json.loads(response)
            except json.JSONDecodeError:
                self._add_error(error=error_invalid_json)
        return response