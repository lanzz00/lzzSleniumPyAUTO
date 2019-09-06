#_author_="lzz"
#coding=utf-8
from appium import webdriver
import time
#义乌网格
#appPackage="cn.com.pubinfo.szzet"
#appActivity="cn.com.pubinfo.emergency.pad.sgt.module.login.LoginActivity"
#省执法
appPackage="com.hesc.escle.sheng.localserver"
appActivity="com.hesc.escle.sheng.module.login.LoginActivity"
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
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'huawei-kiw_al10-QMS0216601005370'
#desired_caps['app']='D:\software\Android\APPS\com.tencent.mm_621.apk'，这个是要安装的app的安装包地址，不是必须的，有#这个项的话会先通过这个地址安装app，我没有用这个，直接用的Package名和activity名
desired_caps['appPackage'] = appPackage
desired_caps['appActivity'] = appActivity
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
#启动
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)

el_name = driver.find_element_by_id("com.hesc.escle.sheng.localserver:id/edt_username")
el_name.clear()
el_name.send_keys("15305713032")
el_psw= driver.find_element_by_id("com.hesc.escle.sheng.localserver:id/edt_password")
el_psw.clear()
el_psw.send_keys("a123456")
el_loginbtn = driver.find_element_by_id("com.hesc.escle.sheng.localserver:id/btn_login")
el_loginbtn.click()
time.sleep(5)