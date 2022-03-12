"""Tests for decorator."""

import sys
from io import StringIO
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
    def fx(self):
        """Test always ok!."""
        return "fx"

    def setUp(self):
        """Session setup."""
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_name(self):
        """Test name."""
        self.assertEqual("xpto", self.xpto.__name__)
        self.assertEqual("fx", self.fx.__name__)

    def test_doc(self):
        """Test doc."""
        self.assertEqual("This ok!", self.xpto.__doc__)
        self.assertEqual("This ok!", self.fx.__doc__)

    def test_return(self):
        """Test return."""
        self.assertEqual(0, self.xpto())
        self.assertEqual("fx", self.fx())

    def test_output(self):
        """Test output."""
        self.xpto()
        output = sys.stdout.getvalue().strip()
        self.assertNotEqual("", output)

    def test_output_mock0(self):
        """Test output with mock."""
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            self.xpto()
            self.assertRegex(
                fakeOutput.getvalue().strip(), r"^xpto: \d*.?\d+ ms$"
            )

    def test_output_mock1(self):
        """Test output with mock."""
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            self.fx()
            self.assertRegex(
                fakeOutput.getvalue().strip(), r"^fx: \d*.?\d+ ms$"
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
            sys.stdout.getvalue(), r"^{}: \d*.?\d+ ms$".format(this.__name__)
        )

    def test_output2(self):
        """Test output."""
        this = self.fx
        this()
        self.assertRegex(
            sys.stdout.getvalue(), r"^{}: \d*.?\d+ ms$".format(this.__name__)
        )


if __name__ == "__main__":
    main()
