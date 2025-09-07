"""Testes para o módulo cpf_cnpj.py."""

import pytest

from incolume.py.utils import cpf_cnpj


class TestCpfCnpj:
    """Testes para o módulo cpf_cnpj.py."""

    @pytest.mark.parametrize(
        'value, expected',
        [
            ('123.456.789-09', '12345678909'),
            ('12345678909', '12345678909'),
            ('12.345.678/0001-95', '12345678000195'),
            ('12345678000195', '12345678000195'),
            ('abc123def456ghi789jk09', '12345678909'),
            ('!@#12$%34^56&*78(90)9', '12345678909'),
            ('', ''),
            (None, ''),
        ],
    )
    def test_only_number(self, value, expected):
        """Testa a função only_number."""
        assert cpf_cnpj.only_number(value) == expected

    @pytest.mark.parametrize(
        'value, expected',
        [
            ('123.456.789-09', '678909'),
            ('12345678909', '678909'),
            ('12.345.678/0001-95', '000195'),
            ('12345678000195', '000195'),
            ('abc123def456ghi789jk09', '678909'),
            ('!@#12$%34^56&*78(90)09', '789009'),
            ('12345', '12345'),  # Menos de 6 dígitos
            ('', ''),  # String vazia
            (None, ''),  # None
        ],
    )
    def test_get_inscription(self, value, expected):
        """Testa a função get_inscription."""
        assert cpf_cnpj.get_inscription(value) == expected

    @pytest.mark.parametrize(
        'value, expected',
        [
            (12345678909, '123.456.789-09'),
            ('12345678909', '123.456.789-09'),
            ('123.456.789-09', '123.456.789-09'),
            ('12345678', '12345678'),  # Menos de 11 dígitos
            ('', ''),  # String vazia
            (None, ''),  # None
            ('123 456 789 09', '123.456.789-09'),
            ('123-456-789-09', '123.456.789-09'),
        ],
    )
    def test_format_cpf(self, value, expected):
        """Testa a função format_cpf."""
        assert cpf_cnpj.format_cpf(value) == expected
