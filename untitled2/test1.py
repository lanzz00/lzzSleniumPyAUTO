# encoding = utf-8
import unittest
'''import random
class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def runTest(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

class TestDictValueFormatFuntions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq,range(10))
        self.assertRaises(TypeError,random.shuffle,(1,2,3))

if __name__ == "__main__":
    unittest.main()

class myclass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b
class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "-------------setUpClass"

    @classmethod
    def tearDownClass(cls):
        print "-------------tearDownClass"

    def setUp(self):
        self.a = 3
        self.b =1
        print "---------setUp"

    def tearDown(self):
        print "----------teardown"

    def testsum(self):
        self.assertEqual(myclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        self.assertEqual(myclass.sub(self.a, self.b), 2, 'test sub fail')

if __name__ == "__main__":
    unittest.main()
'''
import random
import sys
class TestSequenceFunctions(unittest.TestCase):
    a = 1
    def setUp(self):
        self.seq = list(range(10))
    def tearDown(self):
        pass
    @unittest.skipIf(a>5,"condition is not satidfied")
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq,20)
        for elemrnt in random.sample(self.seq,5):
            self.assertTrue(elemrnt in self.seq)
    @unittest.skip("skipping")
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

class TestDictValueFormatFuntions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    def tearDown(self):
        pass



if __name__ == "__main__":
    testcase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    #testcase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFuntions)
    suite = unittest.TestSuite(testcase1)
    unittest.TextTestRunner(verbosity=2).run(suite)


