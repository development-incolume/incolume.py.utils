from pathlib import Path
from tempfile import gettempdir

import pytest

from incolumepy.utils.changelog import (
    changelog_messages,
    changelog_write,
    msg_classify,
    update_changelog,
)

__author__ = "@britodfbr"  # pragma: no cover


class TestCase1:
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
            {},
        ),
    )
    def test_changelog_write(self, entrance, ftemp, return_git_tag):
        result = changelog_messages(text=return_git_tag)
        entrance.update({"content": result})
        if "changelog_file" not in entrance:
            entrance.update({"changelog_file": ftemp})
        assert changelog_write(**entrance)

    @pytest.mark.parametrize(
        "entrance",
        (
            {},
            {"changelog_file": None},
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
