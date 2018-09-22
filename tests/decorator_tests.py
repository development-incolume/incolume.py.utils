from incolumepy.utils.decorators import time_it
from unittest import TestCase, main


class DecoratorTests(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @time_it
    def xpto(self):
        ''' This ok! '''
        n = 0
        for i in range(100000):
            n *= i**2
        return n

    def setUp(self):
        pass

    def test_name(self):
        self.assertAlmostEqual('xpto', self.xpto.__name__)

    def test_doc(self):
        self.assertEqual('This ok!', self.xpto.__doc__)

    def test_output(self):
        print(self.xpto())


if __name__ == '__main__':
    main
