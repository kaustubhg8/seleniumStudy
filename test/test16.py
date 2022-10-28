"""download a file"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "D:\scrap"})
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe", chrome_options=chromeOptions)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#download text file
driver.find_element_by_id("textbox").send_keys("Hello Kaustubh, this is text file")
time.sleep(3)
driver.find_element_by_id("createTxt").click()
time.sleep(3)
driver.find_element_by_id("link-to-download").click()
time.sleep(3)

#download pdf file
driver.find_element_by_id("pdfbox").send_keys("this is pdf file")
time.sleep(3)
driver.find_element_by_id("createPdf").click()
time.sleep(3)
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(5)
driver.close()
