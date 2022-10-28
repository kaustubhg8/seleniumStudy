"""mouse actions"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10) #seconds
driver.maximize_window()
time.sleep(3)
button = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
time.sleep(3)


actions = ActionChains(driver)

actions.double_click(button).perform()
time.sleep(3)
#driver.close()
