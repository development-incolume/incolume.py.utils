from time import time
from functools import wraps


def time_it(func):
    @wraps
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('{}: {}"'.format(func.__name__, end-start))
        return result
    return wrapper

