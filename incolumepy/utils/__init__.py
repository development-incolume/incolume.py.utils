"""incolumepy.utils module."""
import logging
import os
import re
import subprocess
from collections import OrderedDict
from functools import wraps
from pathlib import Path

import toml

confproject = Path(__file__).parents[2] / "pyproject.toml"
versionfile = Path(__file__).parent / "version.txt"
try:
    versionfile.write_text(toml.load(confproject)["tool"]["poetry"]["version"] + "\n")
except FileNotFoundError:
    pass

__version__ = versionfile.read_text().strip()

__title__ = "incolumepy.utils"
# __namespace__ = namespace(__title__)
__name__ = __title__.rsplit(".", maxsplit=1)[-1]


def key_versions_2_sort(x: (tuple, list), qdig: int = 0, regex: str = "") -> str:
    """
    Sort by SemVer notation.

    :param regex: regex to version format.
    :param qdig: Quantity digits to sort.
    :param x: 'git tag -ln' output
    :return: list sorted
    """
    qdig = qdig or 5
    assert isinstance(x, (tuple, list))
    classifies = {
        "post": 4 * 10 ** qdig,
        "rc": 3 * 10 ** (qdig - 1),
        "alpha": 2 * 10 ** (qdig - 1),
        "dev": 0,
    }
    # regex = regex or r"(\d{1,4})\.(\d{1,2})\.(\d{1,2})((-\D+)(\d+))?"
    regex = regex or r"(\d+)\.(\d+)\.(\d+)((-\D+)(\d+))?"
    get_major_minor_patch_build = re.compile(regex)
    logging.debug(get_major_minor_patch_build)
    # pegar major, minor e patch
    values = get_major_minor_patch_build.search(x[0])
    major = values.group(1)
    minor = values.group(2)
    patch = values.group(3)
    build = values.group(6)
    # pegar build, se não tiver colocar uma alta 99999
    build = build or "9" * qdig
    logging.debug(f"values.group(5): {values.group(5)}")
    plus = classifies.get(re.sub(r"[-.]", "", str(values.group(5)).lower()), 0)
    logging.debug(f"plus: {plus}")
    build = int(build) + plus
    result = f"{major:0>4}{minor:0>2}{patch:0>2}.{build:0>6}"
    return result


def update_changelog(changelog_file: (str, Path), reverse: bool = True):
    """
    Update Changelog.md file.

    :param reverse: reverse list.
    :param changelog_file:  changelog full filename.
    :return:
    """
    changelog_file = (
        changelog_file if isinstance(changelog_file, Path) else Path(changelog_file)
    )
    conteudo = subprocess.getoutput("git tag -ln")
    logging.info("registros encontrados ..")
    d = OrderedDict()
    for i in conteudo.split(sep="\n"):
        q = i.split()
        d[q[0].strip()] = " ".join(q[1:]).strip()
    logging.info("registros catalogados ..")
    with changelog_file.open("w") as f:
        f.write(f"# CHANGELOG")
        f.write("\n\n")
        f.write("---\n")
        for i in sorted(d.items(), reverse=reverse, key=key_versions_2_sort):
            f.write("- **{}**: {}\n".format(*i))
        f.write("---\n\n")


def logger(str_format="", datefmt="", level=0, filelog=None):
    """Logger function for log."""
    str_format = (
        str_format
        or "%(asctime)s;%(levelname)-8s;%(name)s;%(module)s;%(funcName)s;%(message)s"
    )
    datefmt = datefmt or "%Y/%m/%d %H:%M:%S %z"
    # create logger
    # levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    level = level or logging.DEBUG
    filelog = filelog or Path(__file__).with_suffix(".py")

    logging.basicConfig(
        filename=filelog, level=level, format=str_format, datefmt=datefmt
    )

    console = logging.StreamHandler()
    formatter = logging.Formatter(str_format)
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)

    return logging.getLogger()


def read(*rnames):
    """Return content from file informed in '*rnames'.

    :param rnames:
    :return:
    >>> read(os.path.dirname(__file__), 'version.txt')
    '0.9.4'

    >>> read(os.path.dirname(__file__), 'README')
    'incolumepy.utils'

    """
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read().strip()


def namespace(package_name):
    """Return the namespace from package_name='incolumepy.package.module' ['incolumepy','incolumepy.package'].

    :param package_name: str
    :return: list

    >>> namespace('incolumepy.package.subpackage.module')
    ['incolumepy', 'incolumepy.package', 'incolumepy.package.subpackage']
    >>> namespace('incolumepy.package.module')
    ['incolumepy', 'incolumepy.package']

    >>> namespace('incolumepy.package')
    ['incolumepy']

    >>> namespace('incolumepy')
    ['incolumepy']
    """
    # print(package_name)
    s = package_name.split(".")
    # print(s)
    l = []
    if len(s) > 2:
        inanis = ""
        for item in s[:-1]:
            if inanis:
                inanis = f"{inanis}.{item}"
            else:
                inanis = item
            l.append(inanis)
    elif 0 < len(s) <= 2:
        l = s[:1]
    else:
        raise ValueError("package_name not can be void")

    # if len(package_name)<=0:
    # elif 0 < len(s) <= 2:
    #     l = s[1]
    # else:
    #     for item in s[:-1]:
    #         if l:
    #             l.append('{}.{}'.format(l[-1], item))
    #         else:
    #             l.append(item)
    #             pass
    #         print(l)
    return l
