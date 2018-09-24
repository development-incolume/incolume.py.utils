from incolumepy.utils.decorators import time_it
from unittest import TestCase, main
import sys


class DecoratorTests(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @time_it
    def xpto(self):
        '''This ok!'''
        n = 1
        for i in range(100000):
            n *= i**2
        return n

    @time_it
    def fx(self):
        '''This ok!'''
        return 'fx'

    def setUp(self):
        pass

    def test_name(self):
        self.assertEqual('xpto', self.xpto.__name__)
        self.assertEqual('fx', self.fx.__name__)


    def test_doc(self):
        self.assertEqual('This ok!', self.xpto.__doc__)
        self.assertEqual('This ok!', self.fx.__doc__)

    def test_return(self):
        self.assertEqual(0, self.xpto())
        self.assertEqual('fx', self.fx())

    def test_output(self):
        self.xpto()
        output = sys.stdout.getvalue().strip()
        self.assertEqual('', output)

    def test_output_mock0(self):
        from io import StringIO
        from unittest.mock import patch

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.xpto()
            self.assertRegex(fakeOutput.getvalue().strip(), '^xpto: \d*.?\d+ ms$')

    def test_output_mock1(self):
        from io import StringIO
        from unittest.mock import patch

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.fx()
            self.assertRegex(fakeOutput.getvalue().strip(), '^fx: \d*.?\d+ ms$')

if __name__ == '__main__':
    main()
