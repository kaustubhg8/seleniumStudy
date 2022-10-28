"""Unit Test"""

import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search Test")

    def test_advancedsearch(self):
        print("This is Advanced search Test")

    def test_prepaidRecharge(self):
        print("This is prepaidRecharge Test")

    @unittest.skipIf(1==1,"We can skip the method based on condition")
    def test_postpaidRecharge(self):
        print("This is PostpaidRecharge Test")

    def test_loginByGmail(self):
        print("this is login by Gmail")

    @unittest.skip("Like this you can skip the test with a reason")
    def test_loginByTwitter(self):
        print("this is login by Twitter")

if __name__ == "__main__":
    unittest.main()