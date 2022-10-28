"""Assertion tests"""
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        pagetitle = driver.title
        #self.assertEqual("Google",pagetitle,"Page title is not same")
        #self.assertNotEqual("Yahoo",pagetitle,"Page title is not same")
        #self.assertTrue(pagetitle == "Google")
        self.assertFalse(pagetitle == "Yahoo")

if __name__ == "__main__":
    unittest.TestCase