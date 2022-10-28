"""Windows (Tabs)"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(10) #seconds
print(driver.current_window_handle)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(3)

print(driver.current_window_handle)
print("Test")

Handles = driver.window_handles

for handle in Handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Selenium":
        driver.close()

