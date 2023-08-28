import pytest

@pytest.yield_fixture() # @pytest.fixture() this can also be used
def setup():
    print("Am a before setup method")
    yield # seperator b/w before & after
    print("Am a after setup method")

def test_method1(setup):
    print("Am a Method 1")

def test_method2(setup):
    print("Am a method 2")