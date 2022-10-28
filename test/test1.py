import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver.get("https://www.saucedemo.com/")
driver.get("https://demo.automationtesting.in/Windows.html")
print(driver.title) #return title of the page
print(driver.current_url) #return url of the page

#driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(3)

#driver.close() #close current url

driver.maximize_window()
time.sleep(3)
#driver.quit() #close the browser

driver.get("https://www.facebook.com/")
time.sleep(3)
print(driver.current_url)

driver.back() #go to back page
time.sleep(3)

driver.forward() #go to forward page
time.sleep(2)
driver.close()