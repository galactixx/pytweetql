import pytest

from tests.utils import load_json_file
from omni_parse import parsing

parameters = [
    (
    './tests/data/user_response.json',
    'success',
    None,
    5
    )
]

@pytest.mark.parametrize('path, status, error, num_users', parameters)
def test_tweets(path, status, error, num_users) -> None:
    """Test tweet responses."""
    response = load_json_file(path=path)
    users = parsing.parse_users(response=response)
    assert users.status == status
    assert users.error == error
    assert users.num_users == num_users