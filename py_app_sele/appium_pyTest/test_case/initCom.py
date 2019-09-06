#_author_="lzz"
#coding=utf-8
from appium import webdriver
import time
#义乌网格
class baseTools:
    def __init__(self,appPackage,appActivity):
        self.appPackage = appPackage
        self.appActivity = appActivity
    def get_appPackage(self):
        return self._appPackage

    def get_appActivity(self):
        return self._appActivity
    def set_appPackage(self,appPackage):
        self._appPackage = appPackage
        return self._appPackage

    def set_appActivity(self,appActivity):
        self._appActivity = appActivity
        return self._appActivity

        #appPackage = "cn.com.pubinfo.szzet"
        #appActivity = "cn.com.pubinfo.emergency.pad.sgt.module.login.LoginActivity"
        #省执法
        #appPackage="com.hesc.escle.sheng.localserver"
        #appActivity="com.hesc.escle.sheng.module.login.LoginActivity"
        '''
        desired_caps = {
            'platformName': 'Android',  # 平台名
            'platformVersion': '6.0.1',  # 平台版本号
            'noReset': True,  # 不重置
            'deviceName': 'huawei-kiw_al10-QMS0216601005370',  # 设备名字
            'appPackage': appPackage,  # app包名
            'appActivity': appActivity  # app 主Activity
        }
        '''
    def driverStart(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'huawei-kiw_al10-QMS0216601005370'
        #desired_caps['app']='D:\software\Android\APPS\com.tencent.mm_621.apk'，这个是要安装的app的安装包地址，不是必须的，有#这个项的话会先通过这个地址安装app，我没有用这个，直接用的Package名和activity名
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #启动
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    #id定位
    def elm_id_sentKey(self,id,str):
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys(str)

    def elm_id_click(self,id):
        self.driver.find_element_by_id(id).click()
    #name定位
    def elm_name_sentKey(self, name, str):
        self.driver.find_element_by_name(name).clear()
        self.driver.find_element_by_name(name).send_keys(str)

    def elm_name_click(self,name):
        self.driver.find_element_by_name(name).click()

    #xpath定位
    def elm_xpath_sentKey(self, xpath, str):
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(str)

    def elm_xpath_click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()


    '''
      全屏滑动
          上下滑动 X轴(宽)不变，Y轴(高)交换位置
          左右滑动 Y轴(高)不变，X轴(宽)交换位置
      '''


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
