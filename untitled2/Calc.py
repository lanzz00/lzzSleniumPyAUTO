# coding = utf-8
class Calc(object):
    def add(self, x, y, *d):
        result = x + y
        for i in d:
            result += 1
        return result
    def mul(self, a, b):
        return a * b
