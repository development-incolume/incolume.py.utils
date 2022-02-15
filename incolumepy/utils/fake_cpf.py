"""Fake CPF module."""
# coding: utf-8
from string import digits

from deprecated import deprecated
from rstr import rstr


@deprecated(
    reason="Descontinued, Use Fake package.WARNNING: will be removed 2.0.0 ",
    version="1.6.4",
)
def gen_fake_cpf(formated=True):
    """Cria um Gerador numeros de CPF com 11 digitos não verificados.

    :param formated: True para formatados(000.000.001-91) e False para somente numeros(00000000191)
    :return: string com numero de CPF de 11 digitos 000.000.001-91 ou 00000000191
    """
    while True:
        cpf = rstr(digits, 11)
        if formated:
            yield f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}"
        else:
            yield cpf


if __name__ == "__main__":
    c1 = gen_fake_cpf()
    c2 = gen_fake_cpf(False)
    print([next(c1) for x in range(5)])
    print([next(c2) for x in range(5)])
