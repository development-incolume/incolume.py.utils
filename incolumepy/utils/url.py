"""URL Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import re


def check_url(url: str) -> bool:
    """
    Check URL.

    :param url: Url to check.
    :return: True if valid URL.

    >>> check_url("http://www.example.com")
    True
    >>> check_url("example.com")
    False
    >>> check_url('https://localhost')
    True
    >>> check_url('https://localhost:8080')
    True
    >>> check_url('127.0.0.1')
    False
    >>> check_url('http://127.0.0.1')
    True
    >>> check_url('http://127.0.0.1:3141')
    True
    """
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return True if re.match(regex, url) else False


def identify_dom_url(url: str, lista_dominio: list = None, verboso: bool = False) -> str:
    """
    Locate match standard on url by lista_dominio, ideal for use into pandas.

    :param url: referida url
    :param verboso: verbosity mode
    :param lista_dominio: lista com os dominios default ['planalto', 'camara', 'senado']
    :return: dominio

    >>> identify_dom_url(
    'https://www2.camara.leg.br/legin/fed/carreg_sn/anterioresa1824/\
    cartaregia-39331-10-julho-1818-569289-publicacaooriginal-92518-pe.html'
    )
    'camara'
    >>> identify_dom_url('https://www.planalto.gov.br/ccivil_03/leis/lim/lim-26-8-1826.htm')
    'planalto'
    >>> identify_dom_url('http://legis.senado.leg.br/norma/416863/publicacao/15637291')
    'senado'
    >>> identify_dom_url('https://www.google.com.br')

    >>> identify_dom_url('https://www.google.com.br', ['google'])
    'google'
    >>> identify_dom_url('https://google.com', verboso=True)
    args: (url='https://google.com', lista_dominio=['planalto', 'camara', 'senado'])
    >>> identify_dom_url('https://google.com', ['google'], True)
    args: (url='https://google.com', lista_dominio=['google'])
    'google'
    """
    lista_dominio = lista_dominio or ["planalto", "camara", "senado"]
    if verboso:
        print(f"args: (url: {url}, lista_dominio: {lista_dominio})")
    for dominio in lista_dominio:
        if re.compile(dominio).search(url):
            return dominio
    return ""
