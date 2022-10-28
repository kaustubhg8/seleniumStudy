"""mouse actions"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.implicitly_wait(10) #seconds
driver.maximize_window()
time.sleep(3)
butn1 = driver.find_element_by_xpath("//*[@id='authentication']/span")
action = ActionChains(driver)
action.context_click(butn1).perform()