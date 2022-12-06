"""incolumepy.utils.files module."""

# !/usr/bin/python
# coding: utf-8
import logging
import os
from pathlib import Path

from deprecated import deprecated

__author__ = "@britodfbr"


@deprecated(
    version="1.6.0",
    reason="Replaced for pathlib.Path.glob or pathlib.Path.rglob. WARNNING: will be removed 2.0.0",
)
def ll(path=".", ext=None, string=True, recursive=False):  # pragma: no cover
    """Recursive or single list of file on directory.

    recursive=True return list recursive, string=True return list of string(path+file),
    string=False return list of tuple(path, file)

    :param path: path on Operation System
    :param ext: extention look for  file
    :param string: Bool
    :param recursive: Bool
    :return: absolute path of file

    """
    if (not string and recursive) and not ext:
        return [
            (p, file)
            for p, _, files in os.walk(os.path.abspath(path))
            for file in files
        ]
    elif (not string and recursive) and ext:
        return [
            (p, file)
            for p, _, files in os.walk(os.path.abspath(path))
            for file in files
            if file.lower().endswith(ext)
        ]
    elif (string and recursive) and not ext:
        return [os.path.join(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]
    elif not string and not recursive:
        return [(path, nome) for nome in os.listdir(path) if os.path.isfile(os.path.join(path, nome))]
    else:
        return [
            os.path.join(path, nome)
            for nome in os.listdir(path)
            if os.path.isfile(os.path.join(path, nome))
        ]


def preserve_file(file_orig):
    """
    Get a passed file on parameter and preserve the original content this file.

    :param file_orig: string with path file
    :return: True if sucess.
    """
    raise NotImplemented("Lançamento futuro..")


def realfilename(filebase, ext=None, digits=2, separador=True):
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
