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
