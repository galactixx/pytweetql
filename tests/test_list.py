import pytest

from tests.utils import load_json_file
from omni_parse import parsing

parameters = [
    (
    './tests/data/list_response.json',
    200,
    'Success',
    1
    )
]

@pytest.mark.parametrize('path, status_code, status_message, num_lists', parameters)
def test_error_simple(path, status_code, status_message, num_lists) -> None:
    """Test error responses."""
    response = load_json_file(path=path)
    lists = parsing.parse_lists(response=response)
    assert lists.status_code == status_code
    assert lists.status_message == status_message
    assert lists.num_lists == num_lists