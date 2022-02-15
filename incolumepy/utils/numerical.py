"""Nonexequi test."""
# coding: utf-8
from functools import lru_cache
from math import sqrt

from deprecated import deprecated


@deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
class Sequencia:
    """Sequence classe."""

    class Fibonacci:
        """Sequence fibonacci."""

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __init__(self):
            """Sequence fibonacci number."""
            self.seq = [1, 1]

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __next__(self):
            """Sequence fibonacci number."""
            self.seq.append(sum(self.seq))
            return self.seq.pop(0)

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __iter__(self):
            """Sequence fibonacci number."""
            return Sequencia.Fibonacci()

    class Naturais:
        """Sequence naturals."""

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __init__(self):
            """Sequence naturals number."""
            self.lista = [0]

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __next__(self):
            """Sequence naturals number."""
            self.lista.append(self.lista[0] + 1)
            return self.lista.pop(0)

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __iter__(self):
            """Sequence naturals number."""
            return Sequencia.Naturais()

    class Pares:
        """Sequence pars."""

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __init__(self):
            """Sequence par number."""
            self.lista = [2]

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __next__(self):
            """Sequence par number."""
            self.lista.append(self.lista[0] + 2)
            return self.lista.pop(0)

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __iter__(self):
            """Sequence par number."""
            return Sequencia.Pares()

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def ispar(self, num):
            """Sequence par number."""
            return num % 2 == 0

    class Impares:
        """Sequence impars."""

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __init__(self):
            """Sequence par number."""
            self.lista = [1]

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __next__(self):
            """Sequence impar number."""
            self.lista.append(self.lista[0] + 2)
            return self.lista.pop(0)

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __iter__(self):
            """Sequence impar number."""
            return Sequencia.Impares()

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def isimpar(self, num):
            """Sequence impar number."""
            return num % 2 == 1

    class Primos:
        """Sequence primers.

        Números primos são os números naturais maiores que 1 e têm apenas dois divisores diferentes: o 1 e ele mesmo.
        """

        primos = []

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __init__(self):
            """Sequence init primer."""
            self.primos = [2, 3, 5, 7]
            self.seq = Sequencia.Naturais()

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __next__(self):
            """Sequence next primer."""
            while 1:
                value = self.seq.__next__()
                if self.isprimo(value):
                    self.primos.append(value)
                    return self.primos[-1]

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def __iter__(self):
            """Sequence iterator primer."""
            return Sequencia.Primos()

        @deprecated(version="0.9.2", reason="Replaced for incolumepy.sequencias")
        def isprimo(self, numero):
            """
            Primer check.

            :param numero:
            :return:
            """
            if numero in self.primos:
                return True

            if numero <= 1:
                return False

            if Sequencia.Pares().ispar(numero):
                return False

            for i in range(3, numero + 1, 2):

                if i != numero:
                    if numero % i == 0:
                        return False
                    if i > sqrt(numero):
                        continue
                else:
                    self.primos.append(numero)
                    return True


@lru_cache()
def milhar(s: str, sep: str = "") -> str:
    """
    Milhar separator.

    :param s: srt number
    :param sep: separator, default point
    :return: str with 's' separate with 'sep'
    """
    sep = sep or "."
    return s if len(s) <= 3 else f"{milhar(s[:-3], sep)}{sep}{s[-3:]}"


# def Main():
#     print("\nPrimos")
#     a = Sequencia.Primos()
#     for i in range(1, 1051):
#         print(i, a.__next__())


if __name__ == "__main__":
    pass
    # Main()
