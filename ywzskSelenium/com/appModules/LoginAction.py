from com.pageObject.LoginPage import LoginPage
from selenium import webdriver
import time

class LoginAction(object):
    def __init__(self):
        print '--login--'

    @staticmethod
    def login(driver,username,password):
        try:
            login = LoginPage(driver)
            login.userNameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginBtn().click()
        except Exception,e:
            raise e

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "http://192.168.86.99:8081/knowledge/#/login2"
    driver.get(url)
    time.sleep(5)
    LoginAction.login(driver,username="admin",password="hesc123456")
    time.sleep(5)
    driver.quit()
