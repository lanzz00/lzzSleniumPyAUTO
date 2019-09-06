# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
url = "http://192.168.86.99:8081/knowledge/#/login2"
driver.get(url)
time.sleep(3)
usernameIpt = driver.find_element_by_class_name("username")
usernameIpt.clear()
usernameIpt.send_keys("admin")
pwdIpt = driver.find_element_by_class_name("password")
pwdIpt.clear()
pwdIpt.send_keys("hesc123456")
pwdIpt.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
#//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/input
searchXpath = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/input')
searchXpath.send_keys(Keys.CONTROL,"a")
searchXpath.send_keys(Keys.DELETE)
searchXpath.send_keys("test")
searchBtn = driver.find_element_by_class_name("header-search-btn")
searchBtn.click()
time.sleep(10)
driver.quit()



