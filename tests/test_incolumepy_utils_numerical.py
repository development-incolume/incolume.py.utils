"""Sequences Tests."""
import unittest

import pytest

from incolumepy.utils.numerical import Sequencia, milhar


@pytest.mark.parametrize(
    ["entrance", "expected"],
    [
        ({"s": "1"}, "1"),
        ({"s": "100"}, "100"),
        ({"s": "1000"}, "1.000"),
        ({"s": "10000"}, "10.000"),
        ({"s": f"{10 ** 7}"}, "10.000.000"),
        ({"s": f"{10 ** 7}", "sep": ","}, "10,000,000"),
        ({"s": f"{10 ** 11}", "sep": "-"}, "100-000-000-000"),
        ({"s": f"{10 ** 23}"}, "100.000.000.000.000.000.000.000"),
        ({"s": f"{10 ** 23}", "sep": None}, "100.000.000.000.000.000.000.000"),
        ({"s": f"{10 ** 23}", "sep": ""}, "100.000.000.000.000.000.000.000"),
        ({"s": f"{10 ** 23}", "sep": ","}, "100,000,000,000,000,000,000,000"),
        ({"s": f"{10 ** 23}", "sep": "-"}, "100-000-000-000-000-000-000-000"),
    ],
)
def test_milhar(entrance, expected):
    assert milhar(**entrance) == expected


class UtilsTest(unittest.TestCase):
    """Class tests numbers."""

    @unittest.skip(reason="Obsolete size release 0.9.2")
    def test_primos(self):
        """Test primers numbers."""
        a = Sequencia.Primos()
        l = []

        for i in range(10):
            l.append(a.__next__())
        self.assertTrue(l == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(next(a), 31)
        self.assertEqual(a.__next__(), 37)
        self.assertEqual(a.__next__(), 41)
        self.assertEqual(a.__next__(), 43)
        a = Sequencia.Primos()
        l.clear()
        for i in range(1000):
            l.append(a.__next__())
        self.assertEqual(a.__next__(), 7927)
        self.assertIn(7669, l)
        a = Sequencia.Primos()
        l.clear()
        for i in range(2000):
            l.append(a.__next__())
        self.assertEqual(a.__next__(), 17393)
        self.assertIn(17389, l)
        self.assertFalse(
            a.isprimo(
                4224696333392304878706725602341482782579852840250681098010280137314308584370130707224123599639141511088446087538909603607640194711643596029271983312598737326253555802606991585915229492453904998722256795316982874482472992263901833716778060607011615497886719879858311468870876264597369086722884023654422295243347964480139515349562972087652656069529806499841977448720155612802665404554171717881930324025204312082516817125
            )
        )

        with self.assertRaises(OverflowError):
            a.isprimo(
                422469633339230487870672560234148278257985284025068109801028013731430858437013070722412359963914151108844608753890960360764019471164359602927198331259873732625355580260699158591522949245390499872225679531698287448247299226390183371677806060701161549788671987985831146887087626459736908672288402365442229524334796448013951534956297208765265606952980649984197744872015561280266540455417171788193032402520431208251681712513
            )

    @unittest.skip(reason="Obsolete size release 0.9.2")
    def test_fibonacci(self):
        """Test fibonacci numbers."""
        a = Sequencia.Fibonacci()
        l = []
        for i in range(10):
            l.append(a.__next__())
        self.assertTrue(l == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertTrue(a.__next__() == 89)
        self.assertTrue(a.__next__() == 144)
        self.assertEqual(a.__next__(), 233)
        self.assertEqual(a.__next__(), 377)
        self.assertEqual(a.__next__(), 610)
        self.assertEqual(a.__next__(), 987)
        l.clear()
        for i in range(2000):
            l.append(a.__next__())
        self.assertIn(
            4224696333392304878706725602341482782579852840250681098010280137314308584370130707224123599639141511088446087538909603607640194711643596029271983312598737326253555802606991585915229492453904998722256795316982874482472992263901833716778060607011615497886719879858311468870876264597369086722884023654422295243347964480139515349562972087652656069529806499841977448720155612802665404554171717881930324025204312082516817125,
            l,
        )

    @unittest.skip(reason="Obsolete size release 0.9.2")
    def test_impares(self):
        """Test impars numbers."""
        a = Sequencia.Impares()
        l = []
        for i in range(10):
            l.append(a.__next__())
        self.assertTrue(l == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
        self.assertTrue(a.__next__() == 21)
        self.assertTrue(a.__next__() == 23)
        self.assertTrue(a.__next__() == 25)

    @unittest.skip(reason="Obsolete size release 0.9.2")
    def test_pares(self):
        """Test pars numbers."""
        b = Sequencia.Pares()
        l = list()
        for i in range(10):
            l.append(b.__next__())
        self.assertTrue(l == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        self.assertTrue(b.__next__() == 22)
        self.assertTrue(b.__next__() == 24)
        self.assertTrue(b.__next__() == 26)

    @unittest.skip(reason="Obsolete size release 0.9.2")
    def test_naturais(self):
        """Test Naturals numbers."""
        print("Naturais ")
        a = Sequencia.Naturais()
        self.assertTrue(a.__next__() == 0)
        self.assertTrue(a.__next__() == 1)
        self.assertTrue(a.__next__() == 2)
        self.assertTrue(a.__next__() == 3)
        self.assertTrue(a.__next__() == 4)
        self.assertTrue(a.__next__() == 5)
        self.assertTrue(a.__next__() == 6)
        self.assertTrue(a.__next__() == 7)
        self.assertTrue(a.__next__() == 8)
        self.assertTrue(a.__next__() == 9)
        self.assertTrue(a.__next__() == 10)
        for i in range(10):
            a.__next__()
        self.assertTrue(a.__next__() == 21)
        l = list()
        for i in range(5):
            l.append(a.__next__())
        self.assertTrue(l == [22, 23, 24, 25, 26])


if __name__ == "__main__":
    unittest.main()
