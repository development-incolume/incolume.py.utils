"""Command Line Interface - CLI module."""

from pathlib import Path
from tempfile import gettempdir

import pytest

from incolumepy.utils.cli import changelog, greeting


class TestCLI:
    @pytest.mark.skip
    def test_output(
        self,
    ):
        file = Path(gettempdir()) / "CHANGELOG.md"
        changelog(file_changelog=file)
        assert True

    @pytest.mark.skip
    def test_greeting(self):
        greeting("ops")
