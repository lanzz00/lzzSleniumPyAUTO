# coding = utf-8
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException,TimeoutException
import traceback
from selenium.webdriver.common.keys import Keys

class ywzsk(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://192.168.86.99:8081/knowledge/#/login2"
        self.driver.get(url)
        usernameIpt = self.driver.find_element_by_class_name("username")
        usernameIpt.clear()
        usernameIpt.send_keys("admin")
        pwdIpt =self.driver.find_element_by_class_name("password")
        pwdIpt.clear()
        pwdIpt.send_keys("hesc123456")
        self.driver.find_element_by_class_name("login-btn").click()
        self.driver.implicitly_wait(10)
    def test_search(self):
        #/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/input
        try:
            searchBox = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/input")
            searchBox.send_keys(Keys.CONTROL, "a")
            searchBox.send_keys(Keys.DELETE)
            searchBox.send_keys("test")

            searchBtn = self.driver.find_element_by_class_name("header-search-btn")
            searchBtn.click()
            self.driver.implicitly_wait(10)
            self.assertIn("test", self.driver.page_source, "not in ")
        except NoSuchAttributeException,e:
            print e
            return False
        else:
            return True


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


