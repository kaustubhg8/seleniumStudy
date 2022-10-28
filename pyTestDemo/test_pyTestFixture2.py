import pytest

@pytest.fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")

def testMethod1(setup):
    print("this is test method 1")

def testMethod2(setup):
    print("this is test method 2")