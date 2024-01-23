from typing import List

from pytweetql.twitter.response._base_response import BaseError
from pytweetql.twitter._utils._data_structures import (
    APIError,
    Status
)

def format_errors(errors: List['Error']) -> Status:
    """
    Format errors in pretty way.

    Args:
        errors (List[Error]): The list of error objects:

    Returns:
        Status: The Status with the errors as a formatted message.
    """
    errors_messages = '\n'.join(error.message for error in errors)
    return Status(
        status_code=502,
        message=f'API request error: {errors_messages}'
    )


class Error(BaseError):
    """
    Parsing for an error-related API response.

    Args:
        message (dict): The raw error message dictionary.
    """
    def __init__(self, message: dict):
        super().__init__(message=message)
        self._error = APIError(message=self._message, code=self._code)

    @property
    def error(self) -> APIError:
        """The entire APIError dataclass."""
        return self._error
    
    @property
    def message(self) -> str:
        """The message which describes the error."""
        return self._error.message

    @property
    def code(self) -> int:
        """An integer code associated with the error."""
        return self._error.code