"""mouse actions"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.softwaretestingmaterial.com/mouse-hover-actions-using-selenium/")
driver.implicitly_wait(10) #seconds
driver.maximize_window()
time.sleep(3)
tutorials = driver.find_element_by_xpath("//*[@id='menu-item-7640']/a/span")
time.sleep(3)
selenium = driver.find_element_by_xpath("//*[@id='menu-item-16994']/a")
time.sleep(3)

actions = ActionChains(driver)

actions.move_to_element(tutorials)
time.sleep(3)
actions.move_to_element(selenium).click().perform()