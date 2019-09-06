# coding = utf-8
import unittest
import HTMLTestRunner
import math

class Calc(object):
    def add(self, x, y, *d):
        result = x + y
        for i in d:
            result += i
        return result
    def sub(self, x, y, *d):
        result = x - y
        for i in d :
            result -= i
        return result
class SuiteTestCalc(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    @unittest.skip("skipping")
    def test_Sub(self):
        print "sub"
        self.assertEqual(self.c.sub(100,34,6),60,'---sss---False-----')
    def test_Add(self):
        print "Add"
        self.assertEqual(self.c.add(1,32,56),89,"--------sss------False-------")

class SuiteTestPow(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    #@unittest.skipIf()
    def test_Pow(self):
        print "Pow"
        self.assertEqual(pow(6,3),216,"---s---F---")
    def test_hasattr(self):
        print "hasattr"
        self.assertTrue(hasattr(math,'pow'),"bu cun zai")

if __name__ == "__mian__":
    suite1 = unittest.TestLoader.loadTestsFromTestCase(SuiteTestCalc)
    suite2 = unittest.TestLoader.loadTestsFromTestCase(SuiteTestPow)
    suite = unittest.TestSuite([suite1,suite2])
    filename = "E:\\test.html"
    fp = file(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="report_title", description="Report_description")
    runner.run(suite)