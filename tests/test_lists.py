import pytest

from tests.utils import load_json_file
from pytweetql import parsing

parameters = [
    (
    './tests/data/create_list.json',
    200,
    1
    )
]

@pytest.mark.parametrize('path, status_code, num_lists', parameters)
def test_create_list(path, status_code, num_lists) -> None:
    """Test CreateList response."""
    response = load_json_file(path=path)
    lists = parsing.parse_create_list(response=response)
    assert lists.status_code == status_code
    assert lists.num_lists == num_lists