from functools import wraps


def nonexequi(a_func):
    '''

    :param a_func:
    :return:
    '''
    @wraps(a_func)
    def wrapTheFunction(self):
        return ('Skip: {}'.format(a_func.__name__))

    return wrapTheFunction


# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
