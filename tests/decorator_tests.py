"""Tests for decorator."""

import sys
import io

from unittest import TestCase, main
from unittest.mock import patch

from incolumepy.utils.decorators import time_it


class DecoratorTests(TestCase):
    """Class for decorator tests."""

    @classmethod
    def setUpClass(cls):
        """Class setup."""

    @time_it
    def xpto(self):
        """Test for xpto."""
        n = 1
        for i in range(100000):
            n *= i ** 2
        return n

    @time_it
    def func_x(self):
        """Test always ok!."""
        return "func_x"

    def setUp(self):
        """Session setup."""
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def test_name(self):
        """Test name."""
        self.assertEqual("xpto", self.xpto.__name__)
        self.assertEqual("func_x", self.func_x.__name__)

    def test_doc(self):
        """Test doc."""
        self.assertEqual("This ok!", self.xpto.__doc__)
        self.assertEqual("This ok!", self.func_x.__doc__)

    def test_return(self):
        """Test return."""
        self.assertEqual(0, self.xpto())
        self.assertEqual("func_x", self.func_x())

    def test_output(self):
        """Test output."""
        self.xpto()
        output = sys.stdout.getvalue().strip()
        self.assertNotEqual("", output)

    def test_output_mock0(self):
        """Test output with mock."""
        with patch("sys.stdout", new=io.StringIO()) as fakeoutput:
            self.xpto()
            self.assertRegex(
                fakeoutput.getvalue().strip(), r"^xpto: \d*.?\d+ ms$"
            )

    def test_output_mock1(self):
        """Test output with mock."""
        with patch("sys.stdout", new=io.StringIO()) as fakeoutput:
            self.func_x()
            self.assertRegex(
                fakeoutput.getvalue().strip(), r"^func_x: \d*.?\d+ ms$"
            )

    def test_output0(self):
        """Test output."""
        self.xpto()
        self.assertRegex(sys.stdout.getvalue(), r"^xpto: \d*.?\d+ ms$")

    def test_output1(self):
        """Test output."""
        this = self.xpto
        this()
        self.assertRegex(
            sys.stdout.getvalue(), rf"^{this.__name__}: \d*.?\d+ ms$"
        )

    def test_output2(self):
        """Test output."""
        this = self.func_x
        this()
        self.assertRegex(
            sys.stdout.getvalue(), rf"^{this.__name__}: \d*.?\d+ ms$"
        )


if __name__ == "__main__":
    main()
