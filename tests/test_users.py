import pytest

from tests.utils import load_json_file
from pytweetql import parsing

parameters_following = [
    (
    './tests/data/following.json',
    200,
    4
    )
]

parameters_user_by_screen_name = [
    (
    './tests/data/user_by_screen_name.json',
    200,
    5
    )
]

parameters_list_members = [
    (
    './tests/data/list_members.json',
    200,
    2
    )
]

parameters_user_by_id = [
    (
    './tests/data/user_by_rest_id.json',
    200,
    1
    )
]

parameters_users_by_ids = [
    (
    './tests/data/users_by_rest_ids.json',
    200,
    1
    )
]

parameters_list_add_member = [
    (
    './tests/data/list_add_member.json',
    200,
    1
    )
]

parameters_list_remove_member = [
    (
    './tests/data/list_remove_member.json',
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


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_following
)
def test_following(path, status_code, num_users) -> None:
    """Test Following responses."""
    response = load_json_file(path=path)
    users = parsing.parse_following(response=response)
    assert users.status_code == status_code
    assert users.num_users == num_users


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_list_add_member
)
def test_list_add_member(path, status_code, num_users) -> None:
    """Test ListAddMember responses."""
    response = load_json_file(path=path)
    users = parsing.parse_list_add_member(response=response)
    assert users.status_code == status_code
    assert users.num_users == num_users


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_list_remove_member
)
def test_list_remove_member(path, status_code, num_users) -> None:
    """Test ListRemoveMember responses."""
    response = load_json_file(path=path)
    users = parsing.parse_list_remove_member(response=response)
    assert users.status_code == status_code
    assert users.num_users == num_users