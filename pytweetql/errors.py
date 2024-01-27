from dataclasses import dataclass

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


def generate_api_error(code: int, message: str) -> Error:
    """Generate dynamic API error from message."""
    return Error(code='ERR_007', message=message, api_code=code)


ERROR_NONE = Error(code='ERR_001', message='Response is null')
ERROR_FORMAT = Error(code='ERR_002', message='Unknown format')
ERROR_JSON = Error(code='ERR_003', message='Invalid JSON')
ERROR_PARSER = Error(code='ERR_004', message='Invalid parser')
ERROR_EMPTY = Error(code='ERR_005', message='Response is empty')
ERROR_API_UNKNOWN = Error(code='ERR_006', message='Unknown API error')