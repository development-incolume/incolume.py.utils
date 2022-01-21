import unittest

from incolumepy.utils.utils import namespace


class UtilsTest(unittest.TestCase):
    def test_namespace1(self):
        self.assertTrue(namespace("incolumepy") == ["incolumepy"])

    def test_namespace2(self):
        self.assertTrue(namespace("incolumepy.package") == ["incolumepy"])

    def test_namespace3(self):
        self.assertTrue(
            namespace("incolumepy.package.subpackage")
            == ["incolumepy", "incolumepy.package"]
        )

    def test_namespace4(self):
        self.assertTrue(
            namespace("incolumepy.package.subpackage.module")
            == ["incolumepy", "incolumepy.package", "incolumepy.package.subpackage"]
        )


if __name__ == "__main__":
    unittest.main()
