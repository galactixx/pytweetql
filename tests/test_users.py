import pytest

from tests.utils import load_json_file
from pytweetql import (
    parsing,
    UserInfo
)

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
    2
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
    UserInfo(
        user_id='44196397',
        user_name='Elon Musk',
        user_screen_name='elonmusk',
        profile_description='(CTO) Chief Troll Officer',
        created='2009-06-02T20:12:29+00:00',
        location='Trōllheim',
        favourites_count=40415,
        followers_count=169898966,
        statuses_count=36635,
        is_verified=True
    )
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
    UserInfo(
        user_id='1744931660808720384',
        user_name='Plutarch Glicia',
        user_screen_name='dandywarlock2',
        profile_description='Lets go to Mars!',
        created='2024-01-10T03:58:29+00:00',
        location='Houston',
        favourites_count=0,
        followers_count=0,
        statuses_count=0,
        is_verified=False
    )
    )
]

parameters_list_remove_member = [
    (
    './tests/data/list_remove_member.json',
    200,
    UserInfo(
        user_id='1744931660808720384',
        user_name='Plutarch Glicia',
        user_screen_name='dandywarlock2',
        profile_description='Lets go to Mars!',
        created='2024-01-10T03:58:29+00:00',
        location='Houston',
        favourites_count=0,
        followers_count=0,
        statuses_count=0,
        is_verified=False
    )
    )
]


@pytest.mark.parametrize(
    'path, status_code, num_users', 
    parameters_user_by_screen_name
)
def test_user_by_screen_name(path, status_code, num_users) -> None:
    """Test UserByScreenName responses."""
    response = load_json_file(path=path)
    users = parsing.parse_users_by_screen_names(response=response)
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
    'path, status_code, user', 
    parameters_user_by_id
)
def test_user_by_id(path, status_code, user) -> None:
    """Test UserByRestId responses."""
    response = load_json_file(path=path)
    single_user = parsing.parse_user_by_id(response=response)
    assert single_user.status_code == status_code
    assert single_user.user.user == user


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
    'path, status_code, user', 
    parameters_list_add_member
)
def test_list_add_member(path, status_code, user) -> None:
    """Test ListAddMember responses."""
    response = load_json_file(path=path)
    single_user = parsing.parse_list_add_member(response=response)
    assert single_user.status_code == status_code
    assert single_user.user.user == user


@pytest.mark.parametrize(
    'path, status_code, user', 
    parameters_list_remove_member
)
def test_list_remove_member(path, status_code, user) -> None:
    """Test ListRemoveMember responses."""
    response = load_json_file(path=path)
    single_user = parsing.parse_list_remove_member(response=response)
    assert single_user.status_code == status_code
    assert single_user.user.user == user