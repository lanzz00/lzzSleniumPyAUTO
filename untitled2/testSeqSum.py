# coding = utf-8
import unittest
class MyTestCse(unittest.TestCase):
    def testEqual(self):
        seq = range(11)
        self.assertEqual(sum(seq),55,'断言列表元素之和结果错误')

