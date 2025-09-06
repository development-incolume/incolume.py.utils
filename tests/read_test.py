"""Read test."""

import unittest

from incolume.py.utils.tools import read
from incolume.py.utils import versionfile


class UtilsTest(unittest.TestCase):
    """Read test."""

    def test_read1(self):
        """Read test."""
        self.assertTrue(read(versionfile))


if __name__ == "__main__":
    unittest.main()
