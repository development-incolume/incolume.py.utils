# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from tempfile import gettempdir

import pytest
import rstr


@pytest.fixture(scope="function")
def temp_file_name():
    return Path(gettempdir()) / rstr.letters(15)
