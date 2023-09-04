"""Command Line Interface - CLI module."""
from pathlib import Path
from tempfile import gettempdir

import pytest
from click.testing import CliRunner

from incolumepy.utils.cli import changelog, greeting


class TestCLI:
    # @pytest.mark.skip
    def test_greeting(self, capsys):
        runner = CliRunner()
        result = runner.invoke(greeting, ["Peter"])
        assert result.exit_code == 0
        assert result.output == "Oi Peter!\n"

    @pytest.mark.parametrize(
        "entrance",
        (
            "# CHANGELOG",
            "[Keep a Changelog]",
            "[Semantic Versioning]",
            "[Conventional Commit]",
            "[incolumepy.utils]",
        ),
    )
    def test_output(self, entrance):
        runner = CliRunner()
        file = Path(gettempdir()) / "CHANGELOG.md"
        fakeurl = "http://fake.incolume.com.br/xpto"
        result = runner.invoke(
            changelog,
            [
                file.as_posix(),
                "-p",
                "false",
                "-u",
                fakeurl,
                "-r",
                "true",
            ],
        )
        assert result
        content = file.read_text()
        assert fakeurl in content
        assert entrance in content
