
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")

links = driver.find_elements(By.TAG_NAME,"a")

print("Number of links present:",len(links))


for link in links:
    #print(link)
    print(link.text)

driver.find_element(By.LINK_TEXT,"Destinations").click()
time.sleep(10)
driver.close()