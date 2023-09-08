"""Command Line Interface - CLI module."""
import sys
from pathlib import Path
from tempfile import gettempdir

import pytest
from click.testing import CliRunner

from incolumepy.utils.cli import (
    changelog,
    digest,
    greeting,
    info,
    info1,
    info2,
    info3,
)


class TestCLI:
    runner = CliRunner()

    @pytest.fixture(scope="function")
    def file(self):
        file = Path(gettempdir()) / "CHANGELOG.md"
        return file

    @pytest.fixture(scope="function")
    def fakeurl(self):
        return "http://fake.incolume.com.br/xpto"

    # @pytest.mark.skip
    def test_greeting(self, capsys):
        result = self.runner.invoke(greeting, ["Peter"])
        assert result.exit_code == 0
        assert result.output == "Oi Peter!\n"

    @pytest.mark.parametrize(
        "args expected".split(),
        (
            ([], sys.platform),
            (["--shout"], "{}!!!!".format(sys.platform.upper())),
        ),
    )
    def test_info(self, args, expected):
        result = self.runner.invoke(info, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        "args expected".split(),
        (
            ([], sys.platform),
            (["--no-shout"], sys.platform),
            (["--shout"], "{}!!!!".format(sys.platform.upper())),
        ),
    )
    def test_info1(self, args, expected):
        result = self.runner.invoke(info1, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        "args expected".split(),
        (
            ([], sys.platform),
            (["--shout"], "{}!!!!".format(sys.platform.upper())),
            (["-S"], sys.platform),
            (["--no-shout"], sys.platform),
        ),
    )
    def test_info2(self, args, expected):
        result = self.runner.invoke(info2, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        "args expected".split(),
        (
            (["--lower"], sys.platform),
            (["--upper"], sys.platform.upper()),
            (["--capitalize"], sys.platform.capitalize()),
        ),
    )
    def test_info3(self, args, expected):
        result = self.runner.invoke(info3, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        "args expected".split(),
        (
            (["--hash-type", "md5"], "MD5"),
            (["--hash-type", "MD5"], "MD5"),
            (["--hash-type", "SHA1"], "SHA1"),
            (["--hash-type", "sha1"], "SHA1"),
        ),
    )
    def test_digest(self, args, expected):
        result = self.runner.invoke(digest, [*args])

        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        "entrance args",
        (
            "# CHANGELOG",
            "[Keep a Changelog]",
            "[Semantic Versioning]",
            "[Conventional Commit]",
            "[incolumepy.utils]",
        ),
    )
    def test_changelog(self, entrance, args, file, fakeurl):
        runner = CliRunner()
        args.extend(["-u", fakeurl, "file", file.as_posix()])
        result = runner.invoke(changelog, args)
        assert result
        content = file.read_text()
        assert fakeurl in content
        assert entrance in content
