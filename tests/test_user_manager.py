import pytest

from app import UserManager


def test_add_and_get_user():
    manager = UserManager()
    payload = {"email": "ada@example.com"}

    manager.add_user("ada", payload)

    assert manager.get_user("ada") == payload


def test_add_existing_user_raises_value_error():
    manager = UserManager()
    manager.add_user("ada", {"email": "ada@example.com"})

    with pytest.raises(ValueError):
        manager.add_user("ada", {"email": "duplicate@example.com"})


def test_remove_user_returns_removed_payload():
    manager = UserManager()
    payload = {"email": "grace@example.com"}
    manager.add_user("grace", payload)

    removed = manager.remove_user("grace")

    assert removed == payload
    assert manager.get_user("grace") is None


def test_remove_missing_user_raises_key_error():
    manager = UserManager()

    with pytest.raises(KeyError):
        manager.remove_user("missing")


def test_list_users_returns_copy():
    manager = UserManager()
    manager.add_user("ada", {"email": "ada@example.com"})

    listed = manager.list_users()
    listed["new"] = {"email": "new@example.com"}

    assert "new" not in manager.list_users()
