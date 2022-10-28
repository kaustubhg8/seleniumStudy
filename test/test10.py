"""Scrolling"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(10) #seconds
driver.maximize_window()
#driver.execute_script("window.scrollBy(0,1000)","")   #scroll down by pixels

#flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)   #scroll down till element
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")    # scroll till end of the page

time.sleep(3)
#driver.close()