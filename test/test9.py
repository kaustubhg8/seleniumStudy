"""Tables"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
driver.implicitly_wait(10) #seconds

rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))            # count no. of rows

colm = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[4]/td"))       # count no. of coloums

print(rows)
print(colm)

print("Company"+"        "+"Contact"+"        "+"Country")
for r in range(2,rows+1):
    for c in range(2,colm+1):
        name = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(name,end='        ')
    print()

driver.close()