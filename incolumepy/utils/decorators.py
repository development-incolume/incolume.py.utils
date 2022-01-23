"""Decorators module."""

from functools import wraps
from time import time


def time_it(func):
    """Retorne a string with execution time.

    :param func: instance of Function
    :return: string in miliseconds
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__}: {1000 * (end - start):3.5f} ms")
        return result

    return wrapper
