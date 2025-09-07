"""Tests for decorator."""

import logging
import re
import tempfile
from inspect import stack
from pathlib import Path

import pytest

from incolume.py.utils.decorators import nonexequi, time_it

# import io
# import sys
# from unittest import TestCase, main
# from unittest.mock import patch


class TestCaseDecoratorNonexequi:
    """Class test for decorator nonexequi."""

    @nonexequi
    def func_x(self):
        """Test for func_x."""
        return stack()[0][3]

    def func_y(self):
        """Test for func_y."""
        return stack()[0][3]

    @pytest.mark.parametrize(
        'entrance',
        (
            'func_x',
            'func_y',
        ),
    )
    def test_name(self, entrance):
        """Test name."""
        assert entrance == getattr(self, entrance).__name__

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        (
            ('func_x', 'Skiped: func_x'),
            ('func_y', 'func_y'),
        ),
    )
    def test_return(self, entrance, expected):
        """Test return."""
        assert getattr(self, entrance)() == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        (
            ('func_x', 'Skiped: func_x'),
            ('func_y', 'func_y'),
        ),
    )
    def test_output(self, entrance, expected, caplog):
        with caplog.at_level(
            logging.DEBUG,
            logger=Path(tempfile.gettempdir()).joinpath('reg.log').as_posix(),
        ):
            result = getattr(self, entrance)()
            assert result == expected
        # assert expected in caplog.text


class TestCaseDecoratorTimeIt:
    """Class test for decorator time_it."""

    @time_it
    def xpto(self):
        """Test for xpto."""
        n = 1
        for i in range(100_000):
            n *= i**2
        return n

    @time_it
    def func_x(self):
        """Test for func_x."""
        return 'func_x'

    @pytest.mark.parametrize(
        'entrance',
        (
            'xpto',
            'func_x',
        ),
    )
    def test_name(self, entrance):
        """Test name."""
        assert entrance == getattr(self, entrance).__name__

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        (
            ('xpto', 'Test for xpto.'),
            ('func_x', 'Test for func_x.'),
        ),
    )
    def test_docstring(self, entrance, expected):
        """Test docstring."""
        assert getattr(self, entrance).__doc__ == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        (
            ('xpto', 0),
            ('func_x', 'func_x'),
        ),
    )
    def test_return(self, entrance, expected):
        """Test return."""
        assert getattr(self, entrance)() == expected

    @pytest.mark.parametrize(
        'entrance',
        (
            'xpto',
            'func_x',
        ),
    )
    def test_output(self, entrance, capsys):
        getattr(self, entrance)()
        out, err = capsys.readouterr()
        assert re.match(rf'^{entrance}: \d*.?\d+ ms$', out, re.IGNORECASE)
        assert err == ''


# class DecoratorTests(TestCase):
#     """Class for decorator tests."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Class setup."""
#
#     def setUp(self):
#         """Session setup."""
#         self.held, sys.stdout = sys.stdout, io.StringIO()
#
#
#     def test_output(self):
#         """Test output."""
#         self.xpto()
#         output = sys.stdout.getvalue().strip()
#         self.assertNotEqual("", output)
#
#     def test_output_mock0(self):
#         """Test output with mock."""
#         with patch("sys.stdout", new=io.StringIO()) as fakeoutput:
#             self.xpto()
#             self.assertRegex(
#                 fakeoutput.getvalue().strip(), r"^xpto: \d*.?\d+ ms$"
#             )
#
#     def test_output_mock1(self):
#         """Test output with mock."""
#         with patch("sys.stdout", new=io.StringIO()) as fakeoutput:
#             self.func_x()
#             self.assertRegex(
#                 fakeoutput.getvalue().strip(), r"^func_x: \d*.?\d+ ms$"
#             )
#
#     def test_output0(self):
#         """Test output."""
#         self.xpto()
#         self.assertRegex(sys.stdout.getvalue(), r"^xpto: \d*.?\d+ ms$")
#
#     def test_output1(self):
#         """Test output."""
#         this = self.xpto
#         this()
#         self.assertRegex(
#             sys.stdout.getvalue(), rf"^{this.__name__}: \d*.?\d+ ms$"
#         )
#
#     def test_output2(self):
#         """Test output."""
#         this = self.func_x
#         this()
#         self.assertRegex(
#             sys.stdout.getvalue(), rf"^{this.__name__}: \d*.?\d+ ms$"
#         )
#
#
# if __name__ == "__main__":
#     main()
