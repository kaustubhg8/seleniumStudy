import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test = None
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        #self.assertIsNone(test)
        self.assertIsNotNone(driver)

    def test2(self):
        list = {"python", "selenium", "java"}
        #self.assertIn("python",list)   #passed
        self.assertNotIn("csharp",list)   #passed

    def test3(self):
        #self.assertGreater(100,10)   #first value > secon value
        #self.assertGreaterEqual(10, 10)   #greater or equal
        #self.assertLess(10,20)
        self.assertLessEqual(10,11)

if __name__ == '__main__':
    unittest.main()