import pytest

@pytest.yield_fixture()
def setup():
    print("Opening url to signup")
    yield
    print("Closing browser after signup")


def test_signupbyemail(setup):
    print("This is a signup by email")

def test_signupbyfacebook(setup):
    print("This is a signup by facebook")