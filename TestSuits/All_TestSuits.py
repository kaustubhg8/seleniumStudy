import unittest
from package1.TC_LoginTest import loginTest
from package1.TC_SignupTest import signupTest
from package2.TC_PaymentTest import PaymentTest
from package2.TC_PaymentReturnsTest import PaymentReturnsTest  #all classes are imported from packages

#get all the tests from classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(loginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(signupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating testsuites

SanityTestSuite = unittest.TestSuite([tc1,tc2])   # Sanity test suite
FunctionalTestSuite = unittest.TestSuite([tc3,tc4])
masterTestSuit = unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(masterTestSuit)
