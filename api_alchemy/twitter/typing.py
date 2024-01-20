from typing import Literal, Union

APIResponse = Union[str, list, dict]
ResponseKey = Union[dict, list]

ParseStatus = Literal['success', 'failure']