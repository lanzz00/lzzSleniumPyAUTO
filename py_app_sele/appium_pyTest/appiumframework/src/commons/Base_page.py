# coding:utf-8
__author__ = 'lanzi'
'''
description:UI页面公共类
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_page:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def send_keys(self,value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def MySwipe(self, direction, n, duration=1000):  # direction为滑动方向（t,d,l,r 四个参数）,
        #  n为滑动次数(n应为整数)    duration 为间隔时间
        if direction == 't':  # top 上滑动
            d = self.driver
            width = d.get_window_size()['width']  # 获取宽度
            height = d.get_window_size()['height']  # 获取高度
            for i in range(n):
                d.swipe(width * 0.5, height * 0.75, width * 0.5, height * 0.25, duration)
        elif direction == 'd':  # down 下滑动
            d = self.driver
            width = d.get_window_size()['width']
            height = d.get_window_size()['height']
            for i in range(n):
                d.swipe(width * 0.5, height * 0.25, width * 0.5, height * 0.75, duration)
        elif direction == 'l':  # left 左滑动
            d = self.driver
            width = d.get_window_size()['width']
            height = d.get_window_size()['height']
            for i in range(n):
                d.swipe(width * 0.75, height * 0.5, width * 0.25, height * 0.5, duration)
        elif direction == 'r':  # right 右滑动
            d = self.driver
            width = d.get_window_size()['width']
            height = d.get_window_size()['height']
            for i in range(n):
                d.swipe(width * 0.25, height * 0.5, width * 0.75, height * 0.5, duration)

