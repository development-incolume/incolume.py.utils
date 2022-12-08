"""incolumepy.utils.files module."""

# !/usr/bin/python
# coding: utf-8
import logging
import os
from pathlib import Path

from deprecated import deprecated

__author__ = "@britodfbr"


def realfilename(
    filebase, ext: str = "", digits: int = 2, separador: bool = True
) -> Path:
    """
    Return real file name for filebase.

    :param filebase: str|pathlib.Path: filename or filebase name or full path
    :param ext: str: extension desert, default (txt)
    :param digits: int: digits of sequence, default 2
    :param separador: bool: default (True)
    :return: pathlib.Path: real filename tip.
    """
    filebase = Path(filebase)
    ext = ext or filebase.suffix or ".txt"
    ext = f".{ext.lstrip('.')}"
    sep = "_" if separador else ""
    filename = filebase.with_name(f"{filebase.stem}{ext}")
    result = filename
    count = 1
    while True:
        result.parent.mkdir(parents=True, exist_ok=True, mode=0o755)
        if not result.is_file():
            logging.debug("Suggested name: %s", result)
            return Path(result)
        dig = f"{count}".zfill(digits)
        result = filename.with_name(f"{filebase.stem}{sep}{dig}{ext}")
        count += 1


@deprecated(
    reason="Hight complexity ciclomatic;"
    " pylint C0209; will be removed in future.",
    version="2.5.3",
)
# pylama:ignore=C901
# flake8: noqa: C0209
def realfilename0(
    filebase,
    ext=None,
    digits=2,
    separador=True
):   # pragma: no cover
    """
    Return real file name for filebase.

    :param filebase:
    :param ext:
    :param digits:
    :param separador:
    :return:
    """
    count = 0
    sufix = {"default": "txt", 0: "txt", 1: None, 2: None}

    if len(filebase.split(".")) > 1:
        prefix = os.path.abspath(os.path.dirname(filebase))
        basename = os.path.basename(filebase)
        # print('1: ', prefix, basename)

        filebase, sufix[1] = basename.split(".")
        # print('2: ', filebase, sufix[1])

        filebase = f"{prefix}/{filebase}"
        # print(filebase, sufix[1])

    if ext:
        sufix[2] = "".join([i for i in ext if i.isalpha()])
        ext = sufix[2]
    elif sufix[1]:
        ext = sufix[1]
    else:
        ext = sufix["default"]

    dir_name = os.path.dirname(filebase)
    # print(dir)
    os.makedirs(os.path.abspath(dir_name), exist_ok=True, mode=0o777)

    if separador:
        sep = "_"
    else:
        sep = ""

    while True:
        try:
            if count <= 0:
                filename = f"{filebase}.{ext}"
            else:
                filename = (
                    "{}{}{:0>%s}.{}" % digits  # pylint: disable=C0209
                ).format(filebase, sep, count, ext)
            if os.path.isfile(filename):
                raise IOError("Arquivo existente: ", filename)
            logging.debug("Nome sugerido: %s", filebase)
            return filename
        except IOError as e:
            logging.warning(e)
        finally:
            count += 1


# pylama:select=C901
