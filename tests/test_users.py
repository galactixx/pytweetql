import pytest

from tests.utils import load_json_file
from omni_parse import parsing

parameters = [
    (
    './tests/data/user_response.json',
    200,
    'Success',
    5
    ),
    (
    './tests/data/user_list_response.json',
    200,
    'Success',
    2
    )
]

@pytest.mark.parametrize('path, status_code, status_message, num_users', parameters)
def test_tweets(path, status_code, status_message, num_users) -> None:
    """Test user responses."""
    response = load_json_file(path=path)
    users = parsing.parse_users(response=response)
    assert users.status_code == status_code
    assert users.status_message == status_message
    assert users.num_users == num_users