from incolumepy.utils.decorators import time_it
from unittest import TestCase, main


class DecoratorTests(TestCase):

    @classmethod
    def setUpClass(cls):
        pass


    def xpto(self):
        '''This ok!'''
        n = 0
        for i in range(100000):
            n *= i**2
        return n

    @time_it
    def fx(self):
        return 'x'

    def setUp(self):
        pass

    def test_name(self):
        self.assertEqual('xpto', self.xpto.__name__)
        # self.assertEqual('fx', self.fx.__name__)

    def test_doc(self):
        self.assertEqual('This ok!', self.xpto.__doc__)
        # self.assertEqual('This ok!', self.fx.__doc__)

    def test_output(self):
        ...


if __name__ == '__main__':
    main
