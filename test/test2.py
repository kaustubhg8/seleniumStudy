import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver.get("https://www.saucedemo.com/")
driver.get("https://demo.guru99.com/test/newtours/")
print(driver.title) #return title of the page
print(driver.current_url) #return url of the page

time.sleep(3)
driver.maximize_window()
time.sleep(1)
print(driver.find_element_by_name("userName").is_displayed())

print(driver.find_element_by_name("password").is_displayed())

print(driver.find_element_by_name("userName").is_enabled())

print(driver.find_element_by_name("password").is_enabled())
time.sleep(1)
driver.find_element_by_name("userName").send_keys("kaustubh")
time.sleep(1)
driver.find_element_by_name("password").send_keys("kaustubh8")
time.sleep(1)
driver.find_element_by_name("submit").click()
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()
time.sleep(5)


roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("Status of round trip radio button ",roundtrip_radio.is_selected())
oneway_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("Status of oneway trip radio button ",oneway_radio.is_selected())

#driver.close()