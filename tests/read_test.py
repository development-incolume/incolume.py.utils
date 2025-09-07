"""Read test."""

import unittest

from incolume.py.utils import versionfile
from incolume.py.utils.tools import read


class UtilsTest(unittest.TestCase):
    """Read test."""

    def test_read1(self):
        """Read test."""
        self.assertTrue(read(versionfile))


if __name__ == '__main__':
    unittest.main()
