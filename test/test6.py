"""Alerts"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(15) #seconds

driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

#driver.switch_to_alert().accept()    #closes alert window using OK button

driver.switch_to_alert().dismiss()    #closes alert window using CANCLE button
driver.sw