"""mouse actions"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(10) #seconds
driver.maximize_window()
time.sleep(3)

rome = driver.find_element_by_xpath("//*[@id='box6']")
italy = driver.find_element_by_xpath("//*[@id='box106']")
actions = ActionChains(driver)
actions.drag_and_drop(rome,italy).perform()
time.sleep(5)
driver.close()
