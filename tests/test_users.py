import pytest

from tests.utils import load_json_file
from pytweetql import parsing

parameters_user_by_screen_name = [
    (
    './tests/data/user_response.json',
    200,
    5
    )
]

parameters_list_members = [
    (
    './tests/data/user_list_response.json',
    200,
    2
    )
]

parameters_user_by_id = [
    (
    './tests/data/user_by_id_response.json',
    200,
    1
    )
]

parameters_users_by_ids = [
    (
    './tests/data/users_by_ids_response.json',
    200,
    1
    )
]


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_user_by_screen_name
)
def test_user_by_screen_name(path, status_code, num_users) -> None:
    """Test UserByScreenName responses."""
    response = load_json_file(path=path)
    users = parsing.parse_users_by_screen_name(response=response)
    assert users.status_code == status_code
    assert users.num_users == num_users


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_list_members
)
def test_list_members(path, status_code, num_users) -> None:
    """Test ListMembers responses."""
    response = load_json_file(path=path)
    users = parsing.parse_list_members(response=response)
    assert users.status_code == status_code
    assert users.num_users == num_users


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_user_by_id
)
def test_user_by_id(path, status_code, num_users) -> None:
    """Test UserByRestId responses."""
    response = load_json_file(path=path)
    users = parsing.parse_user_by_id(response=response)
    assert users.status_code == status_code
    assert users.num_users == num_users


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_users_by_ids
)
def test_users_by_ids(path, status_code, num_users) -> None:
    """Test UsersByRestIds responses."""
    response = load_json_file(path=path)
    users = parsing.parse_users_by_ids(response=response)
    assert users.status_code == status_code
    assert users.num_users == num_users