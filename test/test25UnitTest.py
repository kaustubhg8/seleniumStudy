"""Unit Test"""

import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page is : " + self.driver.title)

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page is : " + self.driver.title)

if __name__=="__main__":
    unittest.main()