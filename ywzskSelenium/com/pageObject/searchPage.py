# coding = utf-8
from com.util.objectMap import *
from com.util.ParseConfigurationFile import ParseCofigFile

class SearchInput(object):
    def __init__(self):
        self.driver = driver
        self.parseCF = ParseCofigFile
    def searchInput(self):
        locateType,locatorExpression = self.parseCF.getOptionValue("ywzsk_search","searchPage.searchElement").split(">")
        elementObj = getElement(self.driver, locateType, locatorExpression)
        return elementObj
    def searchBtn(self):
        locateType,locatorExpression = self.parseCF.getOptionValue("ywzsk_search","searchPage.searchBtn").split(">")
        elementObj = getElement(self.driver, locateType, locatorExpression)
        return elementObj