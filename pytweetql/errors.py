from collections import namedtuple

ValidationError = namedtuple('Error', ['code', 'message'])

ERROR_NONE = ValidationError(code='ERR_001', message='response is null')
ERROR_FORMAT = ValidationError(code='ERR_002', message='unknown format')
ERROR_JSON = ValidationError(code='ERR_003', message='invalid JSON')
ERROR_PARSER = ValidationError(code='ERR_004', message='invalid parser')
ERROR_EMPTY = ValidationError(code='ERR_005', message='response is empty')
ERROR_API_UNKNOWN = ValidationError(code='ERR_006', message='unknown API error')

def generate_api_error(message: str) -> ValidationError:
    """Generate dynamic API error with message."""
    return ValidationError(code='ERR_007', message=message)