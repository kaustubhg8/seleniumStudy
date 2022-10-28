
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
print(driver.title)
driver.implicitly_wait(10) #seconds
driver.maximize_window()

time.sleep(1)
driver.find_element_by_name("userName").send_keys("kaustubh")
time.sleep(1)
driver.find_element_by_name("password").send_keys("kaustubh8")
time.sleep(1)
driver.find_element_by_name("submit").click()
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()
time.sleep(1)

wait =WebDriverWait(driver,10)
oneway_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[value=oneway]")))

oneway_radio.click()

dropdown = driver.find_element("name","fromPort")

ele = Select(dropdown)
time.sleep(3)
ele.select_by_visible_text('Paris')

time.sleep(3)
ele.select_by_index(3)  #new york

time.sleep(3)
ele.select_by_value("London")
time.sleep(3)

print(len(ele.options))

all_options = ele.options
for option in all_options:
    print(option.text)

driver.close()
