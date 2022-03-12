"""Configurate tests."""
# -*- coding: utf-8 -*-
from pathlib import Path
from tempfile import gettempdir

import pytest
import rstr


@pytest.fixture(scope="function")
def temp_file_name():
    """Generate aleatory filename into tempdir for tests."""
    return Path(gettempdir()) / rstr.letters(15)
