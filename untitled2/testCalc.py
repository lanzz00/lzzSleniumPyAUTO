# coding = utf-8
import unittest
from Calc import Calc
class MyClass(unittest.TestCase):
    c = None
    @classmethod
    def setUpClass(cls):
        print u"单元测试前，创建Calc的实例"
        cls.c =Calc()
    def test_add(self):
        print "run add()"
        self.assertEqual(MyClass.c.add(1,2,12),15,"test add fail")