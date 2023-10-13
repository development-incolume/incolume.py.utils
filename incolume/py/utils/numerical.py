"""Nonexequi test."""
# coding: utf-8
from functools import lru_cache


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
