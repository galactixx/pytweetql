import pytest

from tests.utils import load_json_file
from pytweetql import (
    ListInfo,
    parsing
)

parameters = [
    (
    './tests/data/create_list.json',
    200,
    ListInfo(
        name='List name',
        description='Description',
        list_id='1749177315664265474',
        mode='Private',
        member_count=0,
        is_following=True
    )
    )
]

@pytest.mark.parametrize(
    'path, status_code, twitter_list',
    parameters
)
def test_create_list(path, status_code, twitter_list) -> None:
    """Test CreateList response."""
    response = load_json_file(path=path)
    single_list = parsing.parse_create_list(response=response)
    assert single_list.status_code == status_code
    assert single_list.twitter_list.twitter_list == twitter_list