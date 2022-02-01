""" """
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from incolumepy.utils import confproject, versionfile, __version__
__author__ = "@britodfbr"  # pragma: no cover


@pytest.mark.parametrize(
    "entrance",
    (
        confproject,
        versionfile,
    ),
)
def test_file_exist(entrance):
    assert entrance.is_file()
