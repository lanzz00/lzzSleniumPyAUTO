#coding:utf-8
#Edit by liyuanhong 2016/4/12#

#���뵼�������
import sys
curDir = sys.path[0]
print curDir
sys.path.append(curDir + '\\MPTestCases\\common')
sys.path.append(curDir + '/MPTestCases/common')
import Initialize
import CutScreenshot
import traceback


import unittest
from appium import webdriver
from time import sleep
import Initialize

class MPHotpage(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		print "************************** MPHotpage test **************************"
	'''
	def init_case(self):
		#����������Ƿ���ڵ����
		try:
			sleep(1)
			el = self.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #��ȡ��������Ƿ����
			self.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #�����������ϵ�'�������'��ť
			sleep(2)
		except Exception,ex:
			pass
			'''
		
			
	#��ʼ������
	def setUp(self):
		Initialize.setUp(self)

	#��������ִ����ɺ�Ĳ���
	def tearDown(self):
		Initialize.tearDown(self)
		
		
	def click_shouye_rebang_faxian_wo(self):
		try:
			'''��ť�ĵ������
			1���ֱ�Ե׵��ϵ���ҳ���Ȱ񡢷��֣��ҽ����˵��
			'''
			print 'start click_shouye_rebang_faxian_wo test ...  '
			Initialize.init_case(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #����׵��ϵ���ҳ
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_friend').click() #����׵��ϵ��Ȱ�
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_message_tip').click() #����׵��ϵķ���
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #����׵�����
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #����׵��ϵ���ҳ
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
		
	def switch_category_at_shouye_by_click(self):
		try:
			'''��ҳƽ���������
			1������л�����ҳ���еķ���
			'''
			print 'start switch_category_at_shouye_by_click test ...  '
			Initialize.init_case(self)
			sleep(5)
			ele1 = self.driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RadioButton') #��ȡ��ҳ���еĶ�������
			ele1[0].click()
			sleep(2)
			ele1[1].click()
			sleep(2)
			ele1[2].click()
			sleep(2)
			for i in range(0,12):
				ele1[3].click()
				sleep(2)
			ele1[4].click()
			sleep(2)
			ele1[5].click()
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(2)
			self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView').click() #����ر�ȫ��ƽ�����
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)

	def switch_Opencategory_at_shouye_by_click(self):
		try:
			'''��ҳƽ���������
			1������л�����ҳչ����Ƶ������
			'''
			print 'start switch_Opencategory_at_shouye_by_click test ...  '
			Initialize.init_case(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(1)
			ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			for i in range(0,14):
				ele[i].click()
				sleep(1)
				self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
				sleep(1)
			self.driver.swipe(500, 900, 500, 300) #���ϻ���
			ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			ele[len(ele) - 1].click()
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(1)
			ele[len(ele) - 2].click()
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(1)
			self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView').click() #����ر�ȫ��ƽ�����
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)


	def drag_to_change_category_order(self):
		try:
			'''��ҳƽ���������
			1���ı���ҳ�����˳��
			'''
			print 'start drag_to_change_category_order test ...  '
			Initialize.init_case(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(1)
			ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			self.driver.drag_and_drop(ele[6],ele[8])
			sleep(2)
			self.driver.drag_and_drop(ele[4],ele[2])
			sleep(2)
			self.driver.drag_and_drop(ele[8],ele[2])
			sleep(2)
			self.driver.drag_and_drop(ele[4],ele[10])
			sleep(2)
			self.driver.drag_and_drop(ele[10],ele[1])
			sleep(2)
			self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView').click() #����ر�ȫ��ƽ�����
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
		
		
	def switch_category_at_shouye_by_slide(self):
		try:
			'''�л�����ҳ��
			1�������л�����ҳ���еķ���
			'''
			print 'start switch_category_at_shouye_by_slide test ...  '
			Initialize.init_case(self)
			sleep(5)
			for i in range(0,20):
				self.driver.swipe(700, 900, 50, 900) #���һ���
				sleep(2)
			for i in range(0,20):
				self.driver.swipe(50, 900, 700, 900) #���󻬶�
				sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
		
		
		
		
def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPHotpage('click_shouye_rebang_faxian_wo'))
	suite.addTest(MPHotpage('switch_category_at_shouye_by_slide'))
	suite.addTest(MPHotpage('switch_category_at_shouye_by_click'))
	suite.addTest(MPHotpage('switch_Opencategory_at_shouye_by_click'))
	suite.addTest(MPHotpage('drag_to_change_category_order'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)
