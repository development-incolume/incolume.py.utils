import os
import sys
import unittest
import shutil
from incolumepy.utils.files import realfilename


class UtilsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __del__(self, *args, **kwargs):
        pass
        shutil.rmtree(os.path.join(os.path.dirname(__file__), 'tmp'), ignore_errors=True)

    def test_files01(self):
        self.assertTrue(realfilename('version.txt'))

    def test_files02(self):
        self.assertTrue(realfilename('README'))

    def test_files03(self):
        file = realfilename(os.path.join('tmp', 'britodfbr','diretorio', 'para', 'teste'),ext='.dat', separador=True)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files04(self):
        file = realfilename(os.path.join('tmp', 'diretorio', 'para', 'teste'),separador=True, ext='md')
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files05(self):
        file = realfilename(('tmp/teste/test.json'), separador=True, ext='bash')
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files06(self):
        file = realfilename(('tmp/teste/lll'), separador=True)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files07(self):
        file = realfilename(('tmp/teste/jjj.json'), separador=True)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files08(self):
        file = realfilename(os.path.join('tmp', os.path.basename(__file__)), digits=4, ext='log', separador=False)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files09(self):
        file = realfilename(os.path.join('tmp', os.path.basename(__file__)), digits=5, ext='log', separador=True)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files10(self):
        file = realfilename(os.path.join('tmp', os.path.basename(__file__)), digits=5, ext='log')
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))

    def test_files11(self):
        file = realfilename('/tmp/utils/tmp/registro.xml')
        self.assertEqual(sys.stdout.getvalue().strip(), 'Criado arquivo: {}'.format(file))


if __name__ == '__main__':
    unittest.main()