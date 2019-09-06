# coding:utf-8
__author__ = 'lanzi'
'''
description:首页
'''

from appiumframework.src.commons import Base_page
from appium.webdriver.common import mobileby
from appiumframework.src.commons.appCom import baseTools
import time

class myInfo_page(Base_page.Base_page):
    by = mobileby.MobileBy()
    idCaseSB_loc = (by.ID,"cn.com.pubinfo.szzet:id/problem_report_layout")
    idTitle_loc = (by.ID,"cn.com.pubinfo.szzet:id/problem_report_list_detail_title_edittext")
    idType1_loc = (by.ID,"cn.com.pubinfo.szzet:id/problem_report_list_detail_type_textView")
    xpathType1Txt_loc = (by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RadioButton")
    idType2_loc = (by.ID,"cn.com.pubinfo.szzet:id/problem_report_list_detail_secondtype_textView")
    xpathType2Txt_loc = (by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RadioButton")
    idAdress_loc = (by.ID,"cn.com.pubinfo.szzet:id/problem_report_list_detail_address_edittext")
    idSaveBtn_loc = (by.ID,"cn.com.pubinfo.szzet:id/problem_report_list_detail_button_save")
    idwtms_loc = (by.ID,"cn.com.pubinfo.szzet:id/problem_report_list_detail_describe_edittext")
    idimage1_loc = (by.ID,"cn.com.pubinfo.szzet:id/picture_grid")
    idimage2_loc = (by.ID,"android:id/text1")
    idimageList_loc = (by.ID,"com.android.gallery3d:id/list_item_content")
    #点击 首页-问题上报
    def click_caseSBID(self):
        self.find_element(*self.idCaseSB_loc).click()
    time.sleep(3)
    #进入问题上报页面输入问题标题	cn.com.pubinfo.szzet:id/problem_report_list_detail_title_edittext
    def input_idTitle(self,idTitle):
        self.send_keys(idTitle,*self.idTitle_loc)

    #一级类	cn.com.pubinfo.szzet:id/problem_report_list_detail_type_textView
    def click_idType1(self):
         self.find_element(*self.idType1_loc).click()
    def click_xpathType1Txt(self):
         self.find_element(*self.xpathType1Txt_loc).click()
    #二级类	cn.com.pubinfo.szzet:id/problem_report_list_detail_secondtype_textView
    def click_idType2(self):
         self.find_element(*self.idType2_loc).click()
    def click_xpathType2Txt(self):
         self.find_element(*self.xpathType2Txt_loc).click()
    #问题描述
    def input_idwtms(self, idwtms):
        self.send_keys(idwtms, *self.idwtms_loc)

    #上传图片
    def uploadImage(self):
        self.find_element(*self.idimage1_loc).cilck()
        self.find_element(*self.idimage2_loc).cilck()
        image = self.find_element(*self.idimageList_loc)
        image[1].click()

    #页面上滑
    def up_swipe_case(self):

        self.MySwipe(direction="t",n=1,duration=1000)
    #输入事发地点
    def input_idAdress(self, idAdress):
        self.send_keys(idAdress, *self.idAdress_loc)

    #点击保存
    def click_idSaveBtn(self):
        self.find_element(*self.idSaveBtn_loc).click()



