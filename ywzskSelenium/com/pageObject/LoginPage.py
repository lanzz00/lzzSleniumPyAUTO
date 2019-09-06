from com.util.objectMap import *
from selenium import webdriver
from com.util.ParseConfigurationFile import ParseCofigFile
import time
class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.loginOptions = self.parseCF.getItemSection("ywzsk_login")
        print self.loginOptions
        '''
    def switchToFrame(self):
        try:
            #self.driver.switch_to.frame()
            locatorExpression = self.loginOptions["loginPage".lower()].split[1]
            self.driver.switch_to.frame(locatorExpression)
        except Exception,e:
            raise e
    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception,e:
            raise e
        '''
    def userNameObj(self):
        try:
            locateType,locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)

            return elementObj
        except Exception,e:
            raise e

    def passwordObj(self):
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception, e:
            raise e
    def loginBtn(self):
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            elementObj = getElement(self.driver, locateType,locatorExpression)
            return elementObj
        except Exception, e:
            raise e

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "http://192.168.86.99:8081/knowledge/#/login2"
    driver.get(url)
    driver.implicitly_wait(10)
    login = LoginPage(driver)
    login.userNameObj().clear()
    login.userNameObj().send_keys("admin")
    login.passwordObj().clear()
    login.passwordObj().send_keys("hesc123456")
    login.loginBtn().click()
    time.sleep(10)
    driver.quit()
