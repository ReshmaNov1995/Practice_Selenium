import pytest

@pytest.yield_fixture()
def setup():
    print("Opening url to login")
    yield
    print("Closing browser after login")


def test_loginbyemail(setup):
    print("This is a login by email")

def test_loginbyfacebook(setup):
    print("This is a login by facebook")