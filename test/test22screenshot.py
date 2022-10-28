"""Capture screenshot"""

from selenium import webdriver



driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")

driver.maximize_window()
driver.save_screenshot("D:\scrap\seleniumScreenshots\homePage2.png")
driver.get_screenshot_as_file("D:\scrap\seleniumScreenshots\homePage3.jpg")

driver.close()