from time import time
from functools import wraps


def time_it(func):
    @wraps
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('{}: {5:3.2f} ms'.format(func.__name__, 1000*(end-start)))
        return result
    return wrapper
