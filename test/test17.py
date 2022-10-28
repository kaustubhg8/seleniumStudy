"""download a file firefox"""

import time
from selenium import webdriver

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")  #Mime type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","D:\scrap")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)


driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.31.0-win64\geckodriver.exe",
                           firefox_profile=fp)
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
