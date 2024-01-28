from dataclasses import dataclass
from typing import List

@dataclass
class Error:
    """
    A parsing error.

    Attributes:
        code (str): Code associated with the error.
        message (str): Message associated with the error.
        api_code (int, optional): An API code, if the error was generated from the API.
    """
    code: str
    message: str
    api_code: int = None


def is_api_error_specific(code: int, errors: List[Error]) -> bool:
    """Detect if a specific error has occurred, using the API code."""
    return any(error.api_code == code for error in errors)


def is_api_error(error: Error) -> bool:
    """Detect if error is an API error."""
    return error.api_code is not None


def detect_api_errors(errors: List[Error]) -> List[Error]:
    """Get all API errors associated with response."""
    return [error for error in errors if is_api_error(error=error)]


def generate_api_error(code: int, message: str) -> Error:
    """Generate dynamic API error from message."""
    return Error(code='ERR_007', message=message, api_code=code)


ERROR_NONE = Error(code='ERR_001', message='Response is null')
ERROR_FORMAT = Error(code='ERR_002', message='Unknown format')
ERROR_JSON = Error(code='ERR_003', message='Invalid JSON')
ERROR_PARSER = Error(code='ERR_004', message='Invalid parser')
ERROR_EMPTY = Error(code='ERR_005', message='Response is empty')
ERROR_API_UNKNOWN = Error(code='ERR_006', message='Unknown API error')