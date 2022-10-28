import unittest

class signupTest(unittest.TestCase):
    def test_sighupbyEmail(self):
        print("This is sighup by Email Test")
        self.assertTrue(True)

    def test_sighupbyFacebook(self):
        print("This is sighup by Facebook Test")
        self.assertTrue(True)

    def test_sighupbyTwitter(self):
        print("This is sighup by Twitter Test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main