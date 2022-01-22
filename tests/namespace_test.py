"""Namespace testings."""
import unittest

from incolumepy.utils.utils import namespace


class UtilsTest(unittest.TestCase):
    """Class for test namespace."""

    def test_namespace1(self):
        """Assert correct namespace with level 1."""
        self.assertTrue(namespace("incolumepy") == ["incolumepy"])

    def test_namespace2(self):
        """Assert correct namespace with level 2."""
        self.assertTrue(namespace("incolumepy.package") == ["incolumepy"])

    def test_namespace3(self):
        """Assert correct namespace with level 3."""
        self.assertTrue(
            namespace("incolumepy.package.subpackage")
            == ["incolumepy", "incolumepy.package"]
        )

    def test_namespace4(self):
        """Assert correct namespace with level 4."""
        self.assertTrue(
            namespace("incolumepy.package.subpackage.module")
            == ["incolumepy", "incolumepy.package", "incolumepy.package.subpackage"]
        )


if __name__ == "__main__":
    unittest.main()
