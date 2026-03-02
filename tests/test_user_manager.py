import pytest

from app import UserManager


def test_add_user():
    manager = UserManager()
    manager.add_user("adam")
    assert manager.count_users() == 1


def test_add_existing_user():
    manager = UserManager()
    manager.add_user("adam")
    with pytest.raises(ValueError):
        manager.add_user("adam")


def test_remove_user():
    manager = UserManager()
    manager.add_user("Youssef")
    manager.remove_user("Youssef")
    assert manager.count_users() == 0


def test_remove_unknown_user():
    manager = UserManager()

    with pytest.raises(ValueError):
        manager.remove_user("saad")
