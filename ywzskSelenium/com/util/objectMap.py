# coding = utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

def getElement(driver,locateType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by = locateType,value= locatorExpression))
        return element
    except Exception,e:
        raise e

def getElments(driver,locateType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by = locateType,value= locatorExpression))
        return elements
    except Exception,e:
        raise e

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    url = "https://www.baidu.com/"
    driver.get(url)
    searchBox = getElement(driver,"id",'kw')
    print searchBox.tag_name
    alist = getElments(driver,"tag name","a")
    print len(alist)
    driver.quit()