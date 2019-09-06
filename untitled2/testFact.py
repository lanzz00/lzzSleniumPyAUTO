# coding = utf-8
import unittest
from Calc import Calc
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.num = 5

    def testFactorial(self):
        seq = range(1,self.num+1)
        res = reduce(lambda x, y: x * y, seq)
        self.assertEqual(res,120,"断言错误")