import pytest

@pytest.fixture() # this method will be executed before the methods in which this method name is passed as parameter.
def setup():
    print("Am a setup method")

def test_method1(setup):
    print("Am a test method 1")

def test_method2(setup):
    print("Am a test method 2")