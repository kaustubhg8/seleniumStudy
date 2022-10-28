

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10) #seconds
print(driver.title)
assert "Welcome: Mercury Tours" in driver.title

driver.close()
