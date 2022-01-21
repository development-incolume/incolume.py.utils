import re
import unittest

from incolumepy.utils.fake_cpf import gen_fake_cpf


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.cpf1 = gen_fake_cpf(False)
        self.cpf2 = gen_fake_cpf(True)

    def test_fake_cpf1(self):
        self.assertTrue(next(self.cpf1).isdigit())

    def test_fake_cpf2(self):
        self.assertFalse(next(self.cpf2).isdigit())

    def test_fake_cpf3(self):
        cpf = re.split("[.-]", next(self.cpf2))
        # print(cpf)
        self.assertEqual(len(cpf), 4)

    def test_fake_cpf4(self):
        self.assertEqual(len(next(self.cpf1)), 11)

    def test_fake_cpf5(self):
        cpf = next(self.cpf2)
        self.assertRegex(cpf, "\d{3}\.\d{3}\.\d{3}-\d{2}")


if __name__ == "__main__":
    unittest.main()
