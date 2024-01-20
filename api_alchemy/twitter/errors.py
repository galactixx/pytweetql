from api_alchemy.twitter._utils._data_structures import ValidationError

error_response_none = ValidationError(
    code=100,
    error='Response is not of a valid type'
)
error_format_invalid = ValidationError(
    code=101,
    error='Response is not a recognizable format'
)
error_invalid_json = ValidationError(
    code=102,
    error='Response is an invalid JSON'
)
error_invalid_parser = ValidationError(
    code=103,
    error='Invalid parser for response'
)
error_response_empty = ValidationError(
    code=104,
    error='All response fields are empty.'
)