# encoding: utf-8
import unittest
from selenium import webdriver
import time

class GloryRoad(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    @unittest.skip("skipping")
    def testSoGoou(self):
        self.driver.get("https://www.sogou.com/")
        ele_query = self.driver.find_element_by_id("query")
        ele_query.clear()
        ele_query.send_keys("IU")
        ele_stb = self.driver.find_element_by_id("stb")
        ele_stb.click()
        time.sleep(3)
        assert u"IU" in self.driver.page_source,"BU CUN ZAI"
    def test_operateWindowHandle(self):
        url="https://www.baidu.com/"
        self.driver.get(url)
        now_handle = self.driver.current_window_handle
        print now_handle
        kw_input = self.driver.find_element_by_id("kw")
        kw_input.clear()
        kw_input.send_keys("w3cschool")
        su_btn = self.driver.find_element_by_id("su")
        su_btn.click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[2]').click()
        time.sleep(5)
        all_handles = self.driver.window_handles
        print '+++++++',self.driver.window_handles[-1]
        for handle in all_handles:
            if handle != now_handle:
                print handle
        self.driver.switch_to_window(now_handle)

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    testcase = unittest.TestLoader.loadTestsFromTestCase(GloryRoad)
    suite = unittest.TestSuite(testcase)
    suite.run()
    #unittest.main()