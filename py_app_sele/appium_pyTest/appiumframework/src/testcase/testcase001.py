# coding:utf-8
__author__ = 'lanzi'
'''
description:测试登录和退出功能
'''
import unittest
import time

from appiumframework.src.pages import index_page,myInfo_page,login_page,relative_page
from appiumframework.src.commons import gesture_mainpulation
from appiumframework.src.commons import driver_configure

appPackage = "cn.com.pubinfo.szzet"
appActivity = "cn.com.pubinfo.emergency.pad.sgt.module.login.LoginActivity"
class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver(appPackage,appActivity)
        cls.GM = gesture_mainpulation.gesture_mainpulation()

    def test_01login(self):
        '''测试登录功能'''
       # self.index_page = index_page.index_page(self.driver)
        self.login_page = login_page.login_page(self.driver)
        self.login_page.input_user("sxzhz")
        self.login_page.input_Pws("123456")
        self.login_page.click_btnLogin()
        time.sleep(3)
        '''事件上报功能--保存'''
        self.myInfo_page = myInfo_page.myInfo_page(self.driver)
        self.myInfo_page.click_caseSBID()
        self.myInfo_page.input_idTitle("测试-问题标题01")
        self.myInfo_page.click_idType1()
        self.myInfo_page.click_xpathType1Txt()
        self.myInfo_page.click_idType2()
        self.myInfo_page.click_xpathType2Txt()
        self.myInfo_page.input_idwtms("测试-问题描述")
        self.myInfo_page.up_swipe_case()
        self.myInfo_page.uploadImage()
        self.myInfo_page.up_swipe_case()
        self.myInfo_page.input_idAdress("测试-地址01")
        self.myInfo_page.click_idSaveBtn()
        time.sleep(3)
        '''
        # 主页面
        self.index_page = index_page.index_page(self.driver)
        self.index_page.click_btnCancel()
        self.GM.swipe_down(self.driver)
        self.index_page.click_inXSTeach()
        # 我在邢帅
        self.myInfo_page = myInfo_page.myInfo_page(self.driver)
        self.myInfo_page.click_login_btn()
        # 登录页
        self.login_page = login_page.login_page(self.driver)
        self.login_page.input_user("lihailing@xsteqach.com")
        self.login_page.input_Pws("123456")
        self.login_page.click_btnLogin()
        self.assertEqual(u'签到',self.myInfo_page.getText_signHint())
        '''
    '''
    def test_02loginOut(self):
       测试退出功能
        self.myInfo_page = myInfo_page.myInfo_page(self.driver)
        self.myInfo_page.click_relative()
        self.relative = relative_page.relative_page(self.driver)
        self.relative.click_tvLoginOut()
        self.relative.click_btnYes()
        self.assertEqual(u'点击登录',self.myInfo_page.getText_login())
    '''
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()