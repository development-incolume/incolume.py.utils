"""Command Line Interface - CLI module."""

import sys
from pathlib import Path
from tempfile import gettempdir

import pytest
from click.testing import CliRunner

from incolume.py.utils.cli import (
    changelog,
    digest,
    encode,
    greeting,
    info,
    info1,
    info2,
    info3,
)


class TestCLI:
    runner = CliRunner()

    @pytest.fixture(scope='function')
    def file(self):
        file = Path(gettempdir()) / 'CHANGELOG.md'
        return file

    @pytest.fixture(scope='function')
    def fakeurl(self):
        return 'http://fake.incolume.com.br/xpto'

    def test_greeting(self, capsys):
        result = self.runner.invoke(greeting, ['Peter'])
        assert result.exit_code == 0
        assert result.output == 'Oi Peter!\n'

    @pytest.mark.skip(reason='dont ran..')
    def test_encode_input(self):
        result = self.runner.invoke(encode, input='\n')
        assert result.exit_code == 1
        print(result.output)
        expected = 'Password: '
        assert result.output == expected

    @pytest.mark.parametrize(
        ['args', 'expected'],
        (
            (['-p', 'abc123'], True),
            (['--password', 'abc123'], True),
        ),
    )
    def test_encode(self, args, expected, capsys):
        """Test for encode."""
        result = self.runner.invoke(encode, args)
        out, err = capsys.readouterr()
        assert bool(result) == expected
        assert out == ''
        assert err == ''

    @pytest.mark.parametrize(
        ['args', 'expected'],
        (
            ([], sys.platform),
            (['--shout'], f'{sys.platform.upper()}!!!!'),
        ),
    )
    def test_info(self, args, expected):
        result = self.runner.invoke(info, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        ['args', 'expected'],
        (
            ([], sys.platform),
            (['--no-shout'], sys.platform),
            (['--shout'], f'{sys.platform.upper()}!!!!'),
        ),
    )
    def test_info1(self, args, expected):
        result = self.runner.invoke(info1, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        ['args', 'expected'],
        (
            ([], sys.platform),
            (['--shout'], f'{sys.platform.upper()}!!!!'),
            (['-S'], sys.platform),
            (['--no-shout'], sys.platform),
        ),
    )
    def test_info2(self, args, expected):
        result = self.runner.invoke(info2, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        ['args', 'expected'],
        (
            (['--lower'], sys.platform),
            (['--upper'], sys.platform.upper()),
            (['--capitalize'], sys.platform.capitalize()),
        ),
    )
    def test_info3(self, args, expected):
        result = self.runner.invoke(info3, [*args])
        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        ['args', 'expected'],
        (
            (['--hash-type', 'md5'], 'MD5'),
            (['--hash-type', 'MD5'], 'MD5'),
            (['--hash-type', 'SHA1'], 'SHA1'),
            (['--hash-type', 'sha1'], 'SHA1'),
        ),
    )
    def test_digest(self, args, expected):
        result = self.runner.invoke(digest, [*args])

        assert result.exit_code == 0
        assert result.output.strip() == expected

    @pytest.mark.parametrize(
        ['entrance', 'args'],
        (
            pytest.param(
                '# CHANGELOG',
                ['-r', '-p'],
                # marks=pytest.mark.skip,
            ),
            pytest.param(
                '[Keep a Changelog]',
                ['-r'],
                # marks=pytest.mark.skip
            ),
            pytest.param(
                '[Semantic Versioning]',
                ['-r'],
                # marks=pytest.mark.skip
            ),
            pytest.param(
                '[Conventional Commit]',
                ['-r'],
                # marks=pytest.mark.skip
            ),
            pytest.param(
                '[incolumepy.utils]',
                [],
                # marks=pytest.mark.skip
            ),
        ),
    )
    def test_changelog(self, entrance, args, file, fakeurl):
        args.extend(['-u', fakeurl, file.as_posix()])
        result = self.runner.invoke(changelog, args)
        assert result
        content = file.read_text()
        # assert fakeurl in content
        assert entrance in content

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        (
            pytest.param(
                changelog,
                'xpto',
            ),
        ),
    )
    def test_changelog_logging(
        self, entrance, expected, caplog, file, fakeurl
    ):
        result = self.runner.invoke(entrance, ['-p', '-u', fakeurl, file])
        assert result
        assert caplog.records == []
        for log in caplog.records:
            assert log == expected
