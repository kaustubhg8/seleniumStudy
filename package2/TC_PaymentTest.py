import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentinDoller(self):
        print("This is payment in doller Test")
        self.assertTrue(True)

    def test_paymentinRupee(self):
        print("This is payment in Rupee Test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main