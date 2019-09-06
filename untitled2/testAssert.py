# encoding = utf-8
import unittest
import random
import HTMLTestRunner
class MyClass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b
    @classmethod
    def div(cls, a, b):
        return a / b
    @classmethod
    def return_None(cls):
        return None

class MyTest(unittest.TestCase):
    # assertNotEqual()
    def test_assertNotEqual(self):
        try:
            a, b = 5, 2
            res = 3
            self.assertNotEqual(a-b, res, 'sum is fail,%s-%s !=%s' % (a, b, res))
        except AssertionError, e:
            print e

    # assertEqual()
    def test_assertEqual(self):
        try:
            a, b = 1, 2
            sum = 13
            self.assertEqual(a + b, sum, 'sum is fail,%s+%s !=%s' % (a, b, sum))
        except AssertionError, e:
            print e
    # assertTrue()
    def test_asserTrue(self):
        try:
            self.assertTrue(1 == 1,"biao da shi wei jia")
        except AssertionError, e:
            print e
    # assertFalse()
    def test_asserFalse(self):
        try:
            self.assertFalse(2 == 1,"biao da shi wei TRUE")
        except AssertionError, e:
            print e
    #assertIs()
    def test_asserIs(self):
        try:
            a = 12
            b = a
            self.assertIs(a,b,"%s and %s is not object"%(a,b))
        except AssertionError,e:
            print e

if __name__ == "__main__":
    unittest.main()