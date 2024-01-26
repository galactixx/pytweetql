from pytweetql.response._base_response import BaseError
from pytweetql._utils._data_structures import APIError

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