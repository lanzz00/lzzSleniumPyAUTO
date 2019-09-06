# conding = utf-8
from selenium import webdriver
from com.pageObject.LoginPage import LoginPage
from com.appModules.LoginAction import LoginAction
import time

def testSearchLogin():
    try:
        driver = webdriver.Firefox()
        url = "http://192.168.86.99:8081/knowledge/#/login2"
        driver.get(url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        LoginAction.login(driver,"admin","hesc123456")
        time.sleep(8)
        assert u"网站导航" in driver.page_source
    except Exception,e:
        raise e
    finally:
        driver.quit()

if __name__ == "__main__":
    testSearchLogin()
    print u"登陆成功"
