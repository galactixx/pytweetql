from omni_parse.twitter._utils._data_structures import Status

success_response = Status(
    status_code=200,
    message='Success'
)
error_response_none = Status(
    status_code=400,
    message='Response is not of a valid type'
)
error_format_invalid = Status(
    status_code=415,
    message='Response is not in a recognizable format'
)
error_invalid_json = Status(
    status_code=400,
    message='Response is an invalid JSON'
)
error_invalid_parser = Status(
    status_code=500,
    message='Invalid parser for response'
)
error_response_empty = Status(
    status_code=400,
    message='All response fields are empty'
)
error_api_unknown = Status(
    status_code=502,
    message=f'API request error: Unknown error'
)