"""Unit Test"""

import unittest

def setUpModule():      #will execute before any class or method
    print("setUpModule")

def tearDownModule():      #will execute after any class or method
    print("tearDownModule")

class AppTesting(unittest.TestCase):
    def test_search(self):
        print("This is search Test")

    def test_advancedsearch(self):
        print("This is Advanced search Test")

    def test_prepaidRecharge(self):
        print("This is prepaidRecharge Test")

    def test_postpaidRecharge(self):
        print("This is PostpaidRecharge Test")

    @classmethod
    def setUp(self):              #this will exicute each time BEFORE all methods
        print("This is setup method")

    @classmethod
    def tearDown(self):              #this will exicute each time AFTER all methods
        print("This is tearDown method")

    @classmethod
    def setUpClass(cls):         #this will exicute only once before start of all methods
        print("This is setUpClass method")

    @classmethod
    def tearDownClass(cls):       #this will exicute only once after all methods
        print("This is tearDownClass method")


if __name__ == "__main__":
    unittest.main()