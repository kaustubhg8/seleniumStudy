import pytest

@pytest.fixture()       #this method will get executed before every method
def setup():
    print("Once before every method")

def testMethod1(setup):
    print("this is test method 1")

def testMethod2():
    print("this is test method 2")