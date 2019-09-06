# coding:utf-8
__author__ = 'lanzi'
'''
description:登录页
'''

from appiumframework.src.commons import driver_configure
from appium.webdriver.common import mobileby

class index_page(driver_configure.driver_configure):
    by = mobileby.MobileBy()

    def get_driver(self):
        driver = self.driver
