"""Browser cookies"""

from selenium import webdriver



driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
cookies = driver.get_cookies()
print(len(cookies))  #print no. of cookies
print(cookies)   # print all the cookies pair

#adding new cookie
cookie = {'name':'MyCookie','value':'123456789'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()   #cookies will be in dictionary format
print(len(cookies))  #print no. of cookies
print(cookies)   # print all the cookies pair

#deleting cookie
driver.delete_cookie("MyCookie")

cookies = driver.get_cookies()   #cookies will be in dictionary format
print(len(cookies))  #print no. of cookies
print(cookies)

driver.close()