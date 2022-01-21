import logging
import os
import shutil
import sys
import unittest

from incolumepy.utils.files import ll, realfilename


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.directories = []

    def tearDown(self):
        for dir in self.directories:
            # print(dir)
            shutil.rmtree(dir, ignore_errors=True)
        # print('finish destructor')

    def test_files01(self):
        self.assertTrue(realfilename("version.txt"))

    def test_files02(self):
        self.assertTrue(realfilename("README"))

    def test_files03(self):
        self.directories.append(
            os.path.join("tmp", "britodfbr", "diretorio", "para", "teste")
        )
        file = realfilename(self.directories[-1], ext=".dat", separador=True)
        self.assertEqual(
            "root: DEBUG: Nome sugerido: {}".format(file), sys.stdout.fileno().strip()
        )

    def test_files04(self):
        self.directories.append(os.path.join("tmp", "diretorio", "para", "teste"))
        file = realfilename(self.directories[-1], separador=True, ext="md")
        print(type(sys.stdout.getvalue()))
        self.assertEqual(
            "root: DEBUG: Nome sugerido: {}".format(file), sys.stdout.getvalue().strip()
        )

    def test_files05(self):
        self.directories.append("tmp/teste/test.json")
        file = realfilename(self.directories[-1], separador=True, ext="bash")
        self.assertEqual(
            sys.stdout.getvalue().strip(), "Criado arquivo: {}".format(file)
        )

    def test_files06(self):
        file = realfilename(("tmp/teste/lll"), separador=True)
        self.assertEqual(
            sys.stdout.getvalue().strip(), "Criado arquivo: {}".format(file)
        )

    def test_files07(self):
        file = realfilename(("tmp/teste/jjj.json"), separador=True)
        self.assertEqual(
            sys.stdout.getvalue().strip(), "Criado arquivo: {}".format(file)
        )

    def test_files08(self):
        file = realfilename(
            os.path.join("tmp", os.path.basename(__file__)),
            digits=4,
            ext="log",
            separador=False,
        )
        self.assertEqual(
            sys.stdout.getvalue().strip(), "Criado arquivo: {}".format(file)
        )

    def test_files09(self):
        file = realfilename(
            os.path.join("tmp", os.path.basename(__file__)),
            digits=5,
            ext="log",
            separador=True,
        )
        self.assertEqual(
            sys.stdout.getvalue().strip(), "Criado arquivo: {}".format(file)
        )

    def test_files10(self):
        file = realfilename(
            os.path.join("tmp", os.path.basename(__file__)), digits=5, ext="log"
        )
        self.assertEqual(
            sys.stdout.getvalue().strip(), "Criado arquivo: {}".format(file)
        )

    def test_files11(self):
        self.directories.append("/tmp/utils/")
        file = realfilename("/tmp/utils/tmp/registro.xml")
        self.assertEqual(
            sys.stdout.getvalue().strip(), "Criado arquivo: {}".format(file)
        )

    def test_files_realfilename01(self):
        self.directories.append(
            os.path.join("tmp", "britodfbr", "diretorio", "para", "teste")
        )
        with open(
            realfilename(self.directories[-1], ext=".dat", separador=True), "w"
        ) as file:
            file.write("teste ok")

    def test_files_realfilename02(self):
        self.directories.append(os.path.join("tmp", "diretorio", "para", "teste"))
        with open(
            realfilename(self.directories[-1], separador=True, ext="md"), "w"
        ) as file:
            file.write("teste ok")

    def test_files_realfilename03(self):
        self.directories.append("tmp/teste/test.json")
        with open(
            realfilename(self.directories[-1], separador=True, ext="bash"), "w"
        ) as file:
            file.write("teste ok")

    def test_files_realfilename04(self):
        self.directories.append("tmp/teste/lll")
        with open(realfilename(self.directories[-1], separador=True), "w") as file:
            file.write("teste ok")

    def test_files_realfilename05(self):
        self.directories.append("tmp/teste/jjj.json")
        with open(realfilename(self.directories[-1], separador=True), "w") as file:
            file.write("teste ok")

    def test_files_realfilename06(self):
        self.directories.append("tmp")
        with open(realfilename(("tmp/teste/jjj.json"), separador=True), "w") as file:
            file.write("teste ok")

    def test_files_realfilename07(self):
        self.directories.append("tmp")
        with open(
            realfilename(
                os.path.join("tmp", os.path.basename(__file__)),
                digits=4,
                ext="log",
                separador=False,
            ),
            "a",
        ) as file:
            file.write(file.name)

    def test_files_realfilename08(self):
        self.directories.append("tmp")
        with open(
            realfilename(
                os.path.join("tmp", os.path.basename(__file__)),
                digits=4,
                ext="log",
                separador=False,
            ),
            "a",
        ) as file:
            file.write(file.name)

    def test_files_realfilename09(self):
        self.directories.append("tmp")
        with open(
            realfilename(
                os.path.join("tmp", os.path.basename(__file__)),
                digits=5,
                ext="log",
                separador=True,
            ),
            "a",
        ) as file:
            file.write(file.name)

    def test_files_realfilename10(self):
        self.directories.append("tmp")
        with open(
            realfilename(
                os.path.join("tmp", os.path.basename(__file__)), digits=5, ext="csv"
            ),
            "a",
        ) as file:
            file.write(file.name)

    def test_files_realfilename11(self):
        self.directories.append("../teste_utils/")
        with open(realfilename("../teste_utils/tmp/registro.xml"), "w") as file:
            file.write(file.name)

    def test_files_ll01(self):
        self.directories.append("tmp/teste1")
        os.mkdir(self.directories[-1], mode=0o777)

    def test_files_ll02(self):
        self.directories.append("tmp/teste1")
        result = []
        for i in range(3):
            with open(
                realfilename(os.path.join(self.directories[-1], "file")), "w"
            ) as file:
                file.write(file.name)

        # print('>', ll(self.directories[-1], string=False))
        for i, j in ll(self.directories[-1], string=False):
            result.append(j)
        # print('>', result)
        self.assertTrue(result, "['file_01.txt', 'file.txt', 'file_02.txt']")

    def test_files_ll03(self):
        pass

    @staticmethod
    def main():
        super().main()


if __name__ == "__main__":
    unittest.main()
