# coding:utf-8
__author__ = 'lanzi'
'''
description:登录页
'''

from appiumframework.src.commons import Base_page
from appium.webdriver.common import mobileby

class login_page(Base_page.Base_page):
    by = mobileby.MobileBy()
    etUser_loc = (by.ID,"cn.com.pubinfo.szzet:id/login_userName")
    etPws_loc = (by.ID,"cn.com.pubinfo.szzet:id/login_password")
    btnLogin_loc = (by.ID,"cn.com.pubinfo.szzet:id/loginButton")

    def input_user(self,username):
        self.send_keys(username,*self.etUser_loc)

    def input_Pws(self,password):
        self.send_keys(password,*self.etPws_loc)

    def click_btnLogin(self):
        self.find_element(*self.btnLogin_loc).click()