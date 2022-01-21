import sys
from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch

from incolumepy.utils.decorators import time_it


class DecoratorTests(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @time_it
    def xpto(self):
        """This ok!"""
        n = 1
        for i in range(100000):
            n *= i ** 2
        return n

    @time_it
    def fx(self):
        """This ok!"""
        return "fx"

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_name(self):
        self.assertEqual("xpto", self.xpto.__name__)
        self.assertEqual("fx", self.fx.__name__)

    def test_doc(self):
        self.assertEqual("This ok!", self.xpto.__doc__)
        self.assertEqual("This ok!", self.fx.__doc__)

    def test_return(self):
        self.assertEqual(0, self.xpto())
        self.assertEqual("fx", self.fx())

    def test_output(self):
        self.xpto()
        output = sys.stdout.getvalue().strip()
        self.assertNotEqual("", output)

    def test_output_mock0(self):
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            self.xpto()
            self.assertRegex(fakeOutput.getvalue().strip(), "^xpto: \d*.?\d+ ms$")

    def test_output_mock1(self):
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            self.fx()
            self.assertRegex(fakeOutput.getvalue().strip(), "^fx: \d*.?\d+ ms$")

    def test_output0(self):
        self.xpto()
        self.assertRegex(sys.stdout.getvalue(), "^xpto: \d*.?\d+ ms$")

    def test_output1(self):
        this = self.xpto
        this()
        self.assertRegex(
            sys.stdout.getvalue(), "^{}: \d*.?\d+ ms$".format(this.__name__)
        )

    def test_output2(self):
        this = self.fx
        this()
        self.assertRegex(
            sys.stdout.getvalue(), "^{}: \d*.?\d+ ms$".format(this.__name__)
        )


if __name__ == "__main__":
    main()
