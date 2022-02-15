"""incolumepy.utils module."""
from functools import wraps
from pathlib import Path

import toml
import re

from incolumepy.utils.utils import namespace

confproject = Path(__file__).parents[2] / "pyproject.toml"
versionfile = Path(__file__).parent / "version.txt"
try:
    versionfile.write_text(toml.load(confproject)["tool"]["poetry"]["version"] + "\n")
except FileNotFoundError:
    pass

__version__ = versionfile.read_text().strip()

__title__ = "incolumepy.utils"
__namespace__ = namespace(__title__)
__name__ = __title__.rsplit('.', maxsplit=1)[-1]


def key_versions_2_sort(x: (tuple, list)):
    qdig = 5
    assert isinstance(x, (tuple, list))
    classifies = {
        "post": 4 * 10**qdig,
        "rc": 3 * 10 ** (qdig - 1),
        "alpha": 2 * 10 ** (qdig - 1),
        "dev": 0,
    }
    regex = r"(\d{1,4})\.(\d{1,2})\.(\d{1,2})((-\D+)(\d+))?"
    get_major_minor_patch_build = re.compile(regex)
    # print(get_major_minor_patch_build)
    # pegar major, minor e patch
    values = get_major_minor_patch_build.search(x[0])
    major = values.group(1)
    minor = values.group(2)
    patch = values.group(3)
    build = values.group(6)
    # pegar build, se não tiver colocar uma alta 99999
    build = build or "9" * qdig
    # print(f'{values.group(5)=}')
    plus = classifies.get(re.sub(r"[-.]", "", str(values.group(5)).lower()), 0)
    # print(f'{plus=}')
    build = int(build) + plus
    result = f"{major:0>4}{minor:0>2}{patch:0>2}.{build:0>6}"
    return result

