"""Frames"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver.get("https://ui.vision/demo/webtest/frames/")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.implicitly_wait(10) #seconds

driver.switch_to.frame("SingleFrame")  #entre to frame

driver.find_element_by_xpath("/html/body/section/div/div/div/input").send_keys("Hello Kaustubh")

time.sleep(10)
driver.switch_to.default_content()   #get back to main page from frame and then entre into other frame

driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/a").click()