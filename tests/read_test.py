import unittest

from incolumepy.utils.utils import read


class UtilsTest(unittest.TestCase):
    def test_read1(self):
        self.assertTrue(read("version.txt"))

    def test_read2(self):
        self.assertTrue(read("utils.py"))


if __name__ == "__main__":
    unittest.main()
