"""Modulo para tratamento de números de CPF e CNPJ."""

import re


def only_number(ncpf: str) -> str:
    """Retira tudo que não for número do CPF ou CNPJ."""
    return re.sub(r'[^0-9]', '', str(ncpf))


def get_inscription(ncpf: str, count: int = -6):
    """Gerador de inscrição a partir do CPF."""
    return only_number(ncpf)[count:]


def format_cpf(ncpf: str) -> str:
    """Formata o CPF para o formato padrão XXX.XXX.XXX-XX."""
    ncpf = only_number(ncpf)
    if len(ncpf) != 11:
        return ncpf
    return f'{ncpf[:3]}.{ncpf[3:6]}.{ncpf[6:9]}-{ncpf[9:]}'
