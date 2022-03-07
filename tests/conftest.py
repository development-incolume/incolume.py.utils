# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from tempfile import gettempdir
from random import sample
from string import ascii_letters, digits
import pytest


@pytest.fixture(scope='function')
def temp_file_name():
    result = ''.join(sample(digits + ascii_letters, 5))
    return Path(gettempdir()) / result
