#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from itertools import chain


def setUp(driver):
    ele_name = driver.find_element_by_class_name("username")
    ele_pwd = driver.find_element_by_class_name("password")
    ele_name.clear()
    ele_name.send_keys("admin")
    ele_pwd.clear()
    ele_pwd.send_keys("hesc123456")
    ele_login_btn = driver.find_element_by_class_name("login-btn")
    ele_login_btn.click()
    time.sleep(3)


def search(driver, search_name):
    # 定位元素
    ele_serIp = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div[1]/div[2]/input')
    # ele_serbtn = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div[1]/div[3]')
    ele_serbtn = driver.find_element_by_class_name("header-search-btn")
    # ele_serIp.clear()
    # ctrl+a 全选操作
    ele_serIp.send_keys(Keys.CONTROL, 'a')
    # 对全选的内容删除操作
    ele_serIp.send_keys(Keys.DELETE)
    search_name = unicode(search_name, 'UTF-8')
    ele_serIp.send_keys(search_name)
    ele_serbtn.click()
    time.sleep(10)


# new_wenti1.csv   new_quchong.csv    new.csv
# 搜索热词csv文件
path = "E:/testAutoCase/zj_anjianxinjian/py_spider_test/doc/a.csv"
df = pd.read_csv(path)
# 将二重列表转化成一重列表-[['1'],['2'],['3']]转化成['1','2','3']
findle_list = list(chain.from_iterable(df.values.tolist()))
findle_bak_list = findle_list

driver = webdriver.Firefox()
url = "http://192.168.86.94:8081/knowledge/#/login2"
driver.get(url)
setUp(driver)
for i in range(len(findle_bak_list)):
    search(driver, findle_bak_list[i])

driver.quit()