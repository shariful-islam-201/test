import pytest

@pytest.fixture
def setUp():
    print("\nlaunch")
    print("login")
    print("browse")
    yield
    print("logout")
    print("closing")


def testAddItem():
    print("Added")


def testRemoveItem():
    print("Removed")