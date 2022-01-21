from functools import wraps
from os.path import abspath, join, dirname
from incolumepy.utils.utils import namespace, read
from pathlib import Path
import toml

confproject = Path(__file__).parents[2]/"pyproject.toml"
assert confproject.is_file(), "Ops: {}".format(confproject)

versionfile = Path(__file__).parent/"version.txt"
assert versionfile.is_file(), "Ops: {}".format(versionfile)

versionfile.write_text(toml.load(confproject)["tool"]["poetry"]["version"] + "\n")

__version__ = versionfile.read_text().strip()
__title__ = 'incolumepy.utils'
__namespace__ = namespace(__title__)
__name__ = __title__.split('.')[-1]


def nonexequi(a_func):
    ''' This decorator when apply over def, the def dont work, but return a message informing that skip.

    :param a_func: any function
    :return: str = "Skip: a_function_name"
    '''

    @wraps(a_func)
    def wrap_the_function(self):
        return 'Skip: {}'.format(a_func.__name__)

    return wrap_the_function

