from pathlib import Path
from tempfile import gettempdir

import pytest

import incolumepy.utils.changelog
from incolumepy.utils.changelog import (
    Changelog,
    changelog_messages,
    msg_classify,
    update_changelog,
)

__author__ = "@britodfbr"  # pragma: no cover


class TestCase:
    @pytest.mark.parametrize(
        "entrance",
        (
            "1.0.0 Added: Fake record; other fake record; Fixed: Fake fixed",
            "1.3.0 Fixed: Fake record; other fake record; Changed: Fake fixed",
            "2.2.1 Security: Fake record; other fake record; Fake fixed",
            "1.0.5 Added: Fake record; other fake record; Fixed: Fake fixed",
        ),
    )
    def test_msg_classify_type(self, entrance):
        assert isinstance(msg_classify(entrance), dict)

    @pytest.mark.parametrize(
        "entrance",
        (
            "1.0.0 Added: Fake record; other fake record; Fixed: Fake fixed",
            "1.0.5 Added: Fake record; other fake record; Fixed: Fake fixed",
            "1.3.0 Fixed: Fake record; other fake record; Changed: Fake fixed",
            "2.0.0 Security: "
            "Aderência a https://keepachangelog.com/pt-BR/1.0.0/",
            "2.2.1 Security: Fake record; other fake record; Fake fixed",
        ),
    )
    def test_msg_classify_value(self, entrance):
        result = msg_classify(entrance)
        assert "key" in result
        assert "date" in result
        assert "messages" in result

    @pytest.mark.parametrize(
        "entrance expected".split(),
        (
            (
                {
                    "text": """
                    1.0.0 Added: Fake record; other fake; Fixed: Fake fixed",
                    1.3.0 Fixed: Fake record; other fake; Changed: Fake fixed",
                    1.5.0 Added: Fake record; other fake; Fixed: Fake fixed",
                    2.2.0 Security: Fake record; other record; Fake fixed",
                    """
                },
                [
                    (
                        "1.0.0",
                        {
                            "date": "2018-10-19",
                            "key": "1.0.0",
                            "messages": {
                                "Added": ["Fake record", " other fake"],
                                "Fixed": ['Fake fixed",'],
                            },
                        },
                    ),
                    (
                        "1.3.0",
                        {
                            "date": "2022-01-21",
                            "key": "1.3.0",
                            "messages": {
                                "Changed": ['Fake fixed",'],
                                "Fixed": ["Fake record", " other fake"],
                            },
                        },
                    ),
                    (
                        "1.5.0",
                        {
                            "date": "2022-01-22",
                            "key": "1.5.0",
                            "messages": {
                                "Added": ["Fake record", " other fake"],
                                "Fixed": ['Fake fixed",'],
                            },
                        },
                    ),
                    (
                        "2.2.0",
                        {
                            "date": "2022-02-16",
                            "key": "2.2.0",
                            "messages": {
                                "Security": [
                                    "Fake record",
                                    " other record",
                                    ' Fake fixed",',
                                ]
                            },
                        },
                    ),
                ],
            ),
            (
                {
                    "text": "1.0.0 Security: a;b;c; "
                    "Removed: 1;2;3; Changed: a;b;c;d;e; "
                    "Fixed: http://example.com; http://httpbin.com;"
                    "Deprecated: 1;2;3;a;s;b; Added: a1;a2;a3."
                },
                [
                    (
                        "1.0.0",
                        {
                            "key": "1.0.0",
                            "date": "2018-10-19",
                            "messages": {
                                "Added": "a1 a2 a3.".split(),
                                "Changed": "a;b;c;d;e".split(";"),
                                "Deprecated": "1;2;3;a;s;b".split(";"),
                                "Fixed": [
                                    "http://example.com",
                                    " http://httpbin.com",
                                ],
                                "Removed": ["1", "2", "3"],
                                "Security": ["a", "b", "c"],
                            },
                        },
                    )
                ],
            ),
        ),
    )
    def test_changelog_messages(self, entrance, expected):
        assert changelog_messages(**entrance) == expected

    @pytest.mark.parametrize(
        "entrance",
        (
            {"changelog_file": Path(gettempdir()) / "CHANGELOG.md"},
            pytest.param(
                {"changelog_file": None},
                # marks=pytest.mark.skip(
                #     reason='need mock to write CHANGELOG.md')
            ),
            pytest.param(
                {},
            ),
        ),
    )
    def test_changelog_write(self, entrance, ftemp, return_git_tag, mocker):
        result = changelog_messages(text=return_git_tag)
        entrance.update({"content": result})
        if "changelog_file" not in entrance:
            entrance.update({"changelog_file": ftemp})

        mocked = mocker.Mock(spec=incolumepy.utils.changelog.changelog_write)
        result = mocked(**entrance)
        esperado = mocker.call(**entrance)
        assert esperado == mocked.call_args  # cobertura QA
        assert result  # Resultado

    @pytest.mark.parametrize(
        "entrance",
        (
            {},
            {
                "changelog_file": Path(gettempdir())
                .joinpath("xpto.md")
                .as_posix()
            },
        ),
    )
    def test_update_changelog(self, entrance, ftemp, return_git_tag):
        entrance.update({"content": return_git_tag})
        if "changelog_file" not in entrance:
            entrance.update({"changelog_file": ftemp})
        assert update_changelog(**entrance)


class TestClassChangelog:
    @pytest.mark.parametrize(
        "entrance",
        (
            {},
            {"reverse": False},
        ),
    )
    def test_init(self, entrance):
        """Test for init class."""
        o = Changelog(**entrance)
        assert isinstance(o, Changelog)

    @pytest.mark.parametrize(
        "entrance expected".split(),
        (
            (
                {},
                [
                    "# CHANGELOG\n\n\n",
                    "All notable changes to this project",
                    " will be documented in this file.\n\n",
                    "The format is based on ",
                    "[Keep a Changelog]"
                    "(https://keepachangelog.com/en/1.0.0/), ",
                    "this project adheres to [Semantic Versioning]"
                    "(https://semver.org/spec/v2.0.0.html) and "
                    "[Conventional Commit]"
                    "(https://www.conventionalcommits.org/"
                    "pt-br/v1.0.0/).\n\n",
                    "This file was automatically generated for",
                    " [incolumepy.utils]"
                    "(https://gitlab.com/development-incolume/"
                    "incolumepy.utils/-/tree/2.7.1)",
                    "\n\n---\n",
                ],
            ),
            (
                {"reverse": False},
                [
                    "# CHANGELOG\n\n\n",
                    "All notable changes to this project",
                    " will be documented in this file.\n\n",
                    "The format is based on ",
                    "[Keep a Changelog]"
                    "(https://keepachangelog.com/en/1.0.0/), ",
                    "this project adheres to [Semantic Versioning]"
                    "(https://semver.org/spec/v2.0.0.html) and "
                    "[Conventional Commit]"
                    "(https://www.conventionalcommits.org/"
                    "pt-br/v1.0.0/).\n\n",
                    "This file was automatically generated for",
                    " [incolumepy.utils]"
                    "(https://gitlab.com/development-incolume/"
                    "incolumepy.utils/-/tree/2.7.1)",
                    "\n\n---\n",
                ],
            ),
        ),
    )
    def test_header(self, entrance, expected):
        """Test for header file."""
        o = Changelog(**entrance)
        assert o.header() == expected
