# coding: utf-8
import unittest
import sys
from incolumepy.utils import nonexequi


class UtilsTest(unittest.TestCase):
    @nonexequi
    def truncus01(self):
        return True

    def truncus02(self):
        return True

    @nonexequi
    def truncus03(self):
        return True

    def truncus04(self):
        return True

    @nonexequi
    def truncus05(self):
        return True

    def test_nonexequi01(self):
        a = UtilsTest()
        for i in ['truncus{:0>2}'.format(x) for x in range(1,5,2)]:
            #self.assertEqual(sys.stdout.getvalue().strip(), 'Skip: %s' %i)
            self.assertEqual(eval('a.{}'.format(i))(), 'Skip: %s' %i)

    def test_nonexequi02(self):
        a = UtilsTest()
        for i in ['truncus{:0>2}'.format(x) for x in range(1, 5) if x % 2 == 0]:
            # self.assertEqual(sys.stdout.getvalue().strip(), 'Skip: %s' %i)
            self.assertEqual(eval('a.{}'.format(i))(), True)


if __name__ == '__main__':
    unittest.main()

