#coding:utf-8
from selenium import webdriver
import unittest,time
import logging,traceback
import ddt
from selenium.common.exceptions import NoSuchAttributeException

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] % (levelname)s % (message)s',
    datefmt= '%a,%d %b %Y %H :%M %S',
    filename="E:/report.log"
)

@ddt.ddt
class TestDome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    @ddt.data([u"Fantastic Beasts and Where to Find Them",u"David Yates"],
              [u"Zootopia",u"Ginnifer Goodwin"],)
    @ddt.unpack
    def test_dataDriverByOjb(self, testdata, excepctdata):
        url = "https://www.baidu.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            kw_input = self.driver.find_element_by_id("kw")
            kw_input.clear()
            kw_input.send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(excepctdata in self.driver.page_source)

        except NoSuchAttributeException,e:
            logging.error(u"page is not font："+str(traceback.format_exc()))

        except AssertionError,e:
            logging.info(u"search %s,except %s,F" %(testdata,excepctdata))

        except Exception,e:
            logging.error(u"error： "+str(traceback.format_exc()))
        else:
            logging.info(u"search % s ,except % s ,T" %(testdata,excepctdata))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()