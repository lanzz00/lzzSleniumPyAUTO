#_author_="lzz"
#coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from  test_case.initCom import baseTools
import time
#义乌网格

appPackage = "cn.com.pubinfo.szzet"
appActivity = "cn.com.pubinfo.emergency.pad.sgt.module.login.LoginActivity"
baseTools.set_appActivity(appActivity)
baseTools.set_appPackage(appPackage)
driver = baseTools.__init__(appPackage,appActivity)
driver = baseTools.driverStart()
#登录
def login():
    el_name =driver.find_element_by_id("cn.com.pubinfo.szzet:id/login_userName")
    print(el_name.text)
    if len(el_name.text) != 0:
        el_name.clear()
    el_name.send_keys("sxzhz")

    el_psw= driver.find_element_by_id("cn.com.pubinfo.szzet:id/login_password")
    if len(el_psw.text) != 0:
        el_psw.clear()
    el_psw.send_keys("123456")
    el_loginbtn = driver.find_element_by_id("cn.com.pubinfo.szzet:id/loginButton")
    el_loginbtn.click()
    login()
#问题上报
try:
    el_alert = driver.find_element_id("android:id/alertTitle")
except NoSuchElementException as el_alert:
    print("cesh")