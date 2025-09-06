"""Decorators module."""
import logging
from functools import wraps
from time import time


def nonexequi(a_func):
    """Decorate when apply over def.

    the def dont work, but return a message informing that skip.

    :param a_func: any function
    :return: str = "Skip: a_function_name"
    """

    @wraps(a_func)
    def wrap_the_function(*args, **kwargs):
        logging.debug("%s(%s, %s).", a_func.__name__, args, kwargs)
        return f"Skiped: {a_func.__name__}"

    return wrap_the_function


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
