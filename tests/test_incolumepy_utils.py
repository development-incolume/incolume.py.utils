"""Utils tests."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import logging
from collections import OrderedDict
from itertools import repeat

import pytest

from incolume.py.utils import (
    __version__,
    confproject,
    versionfile,
)
from incolume.py.utils.tools import key_versions_2_sort, namespace, update_changelog, logger

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


@pytest.mark.parametrize(
    "entrance expected".split(),
    [
        (("0.5.11", "aaa"), "00000511.099999"),
        (("0.5.11-dev0", "aaa"), "00000511.000000"),
        (("0.5.1-dev9", "aaa"), "00000501.000009"),
        (("0.5.1-dev19", "aaa"), "00000501.000019"),
        (("0.5.1-dev99", "aaa"), "00000501.000099"),
        (("0.5.1-alpha9", "aaa"), "00000501.020009"),
        (("0.5.1-beta9", "aaa"), "00000501.000009"),
        (("0.5.1-rc.9", "aaa"), "00000501.080009"),
        (("0.5.1-rc.1", "aaa"), "00000501.080001"),
        (("0.5.1-rc1", "aaa"), "00000501.080001"),
        (("0.5.1rc1", "aaa"), "00000501.080001"),
        (("0.5.1-alpha.1", "aaa"), "00000501.020001"),
        (("0.5.1-alpha.2", "aaa"), "00000501.020002"),
        (("0.5.1-alpha.3", "aaa"), "00000501.020003"),
        (("0.5.1-alpha.4", "aaa"), "00000501.020004"),
        (("0.5.1-alpha.0", "aaa"), "00000501.020000"),
        (("0.5.1-post.0", "aaa"), "00000501.900000"),
        (("1.5.1-post0", "aaa"), "00010501.900000"),
        (("1.5", "aaa"), "1.5"),
        (("1.5.1-rc.0", "aaa"), "00010501.080000"),
        (("1.5.1-rc0", "aaa"), "00010501.080000"),
        (("1.5.1rc0", "aaa"), "00010501.080000"),
        (("1.5.1-a.0", "aaa"), "00010501.020000"),
        (("1.5.1-a0", "aaa"), "00010501.020000"),
        (("1.5.1a0", "aaa"), "00010501.020000"),
        (("1.5.1", "aaa"), "00010501.099999"),
    ],
)
def test_key_versions_2_sort(entrance, expected):
    assert key_versions_2_sort(entrance) == expected


@pytest.mark.parametrize(
    "entrance reverse expected".split(),
    [
        (
            {
                "2019.5.1": "aaa",
                "2019.5.1-dev9": "aaa",
                "2019.5.1-alpha9": "aaa",
                "2019.5.1-beta9": "aaa",
                "2019.5.1-rc.9": "aaa",
                "2019.5.1-rc1": "aaa",
                "2019.5.1-post0": "aaa",
                "2019.5.0": "aaa",
                "2019.5.2-a.0": "aaa",
            },
            True,
            [
                ("2019.5.2-a.0", "aaa"),
                ("2019.5.1-post0", "aaa"),
                ("2019.5.1", "aaa"),
                ("2019.5.1-rc.9", "aaa"),
                ("2019.5.1-rc1", "aaa"),
                ("2019.5.1-alpha9", "aaa"),
                ("2019.5.1-dev9", "aaa"),
                ("2019.5.1-beta9", "aaa"),
                ("2019.5.0", "aaa"),
            ],
        ),
        (
            {
                "0.1.0": "1",
                "0.1.0-dev.0": "2",
                "0.1.0-post.0": "3",
                "0.1.0-a.1": "4",
                "0.1.0-a.0": "5",
                "0.1.1-a.0": "6",
                "0.1.0-rc.1": "7",
                "0.1.0-rc.2": "8",
            },
            False,
            [
                ("0.1.0-dev.0", "2"),
                ("0.1.0-a.0", "5"),
                ("0.1.0-a.1", "4"),
                ("0.1.0-rc.1", "7"),
                ("0.1.0-rc.2", "8"),
                ("0.1.0", "1"),
                ("0.1.0-post.0", "3"),
                ("0.1.1-a.0", "6"),
            ],
        ),
        pytest.param(
            OrderedDict(
                {
                    "2019.5.1": "aaa",
                    "2019.5.11": "aaa",
                    "2019.5.11-dev0": "aaa",
                    "2019.5.1-dev9": "aaa",
                    "2019.5.1-dev19": "aaa",
                    "2019.5.1-dev99": "aaa",
                    "2019.5.1-alpha9": "aaa",
                    "2019.5.1-beta9": "aaa",
                    "2019.5.1-rc.9": "aaa",
                    "2019.5.1-rc1": "aaa",
                    "2019.5.1-alpha.1": "aaa",
                    "2019.5.1-alpha.2": "aaa",
                    "2019.5.1-alpha.3": "aaa",
                    "2019.5.1-alpha.4": "aaa",
                    "2019.5.1-alpha.0": "aaa",
                    "2019.5.1-post0": "aaa",
                    "2019.5.11-post.0": "aaa",
                    "2019.5.11-dev1": "aaa",
                    "2019.5.2-dev0": "aaa",
                    "2019.5.2-dev1": "aaa",
                    "2019.5.2-dev2": "aaa",
                    "2019.5.2-alpha.0": "aaa",
                    "2019.5.1-dev98": "aaa",
                    "2019.5.2": "aaa",
                    "2019.5.0": "aaa",
                }
            ),
            True,
            [
                ("2019.5.11-post.0", "aaa"),
                ("2019.5.11", "aaa"),
                ("2019.5.11-dev1", "aaa"),
                ("2019.5.11-dev0", "aaa"),
                ("2019.5.2", "aaa"),
                ("2019.5.2-alpha.0", "aaa"),
                ("2019.5.2-dev2", "aaa"),
                ("2019.5.2-dev1", "aaa"),
                ("2019.5.2-dev0", "aaa"),
                ("2019.5.1-post0", "aaa"),
                ("2019.5.1", "aaa"),
                ("2019.5.1-rc.9", "aaa"),
                ("2019.5.1-rc1", "aaa"),
                ("2019.5.1-alpha9", "aaa"),
                ("2019.5.1-alpha.4", "aaa"),
                ("2019.5.1-alpha.3", "aaa"),
                ("2019.5.1-alpha.2", "aaa"),
                ("2019.5.1-alpha.1", "aaa"),
                ("2019.5.1-alpha.0", "aaa"),
                ("2019.5.1-dev99", "aaa"),
                ("2019.5.1-dev98", "aaa"),
                ("2019.5.1-dev19", "aaa"),
                ("2019.5.1-dev9", "aaa"),
                ("2019.5.1-beta9", "aaa"),
                ("2019.5.0", "aaa"),
            ],
            marks=pytest.mark.skipif(False, reason="Waiting.."),
        ),
    ],
)
def test_apply_key_versions_2_sort(entrance, reverse, expected):
    result = sorted(entrance.items(), key=key_versions_2_sort, reverse=reverse)
    assert result == expected


@pytest.mark.skip(reason="Deprecated on 2.6.0a4.")
@pytest.mark.parametrize(
    "str_testing reverse expected".split(),
    [
        pytest.param(
            "0.1.0 system\n0.1.1 Fake record\n0.1.1-alpha.0 Fake record"
            "\n0.1.1-rc.0 Fake record\n0.1.1-rc.1 Fake record"
            "\n0.2.0 Fake record\n0.0.1 Fake record",
            True,
            (
                "# CHANGELOG\n"
                "\n\n"
                "All notable changes to this project will be "
                "documented in this file.\n\n"
                "The format is based on [Keep a Changelog]"
                "(https://keepachangelog.com/en/1.0.0/), "
                "and this project adheres to [Semantic Versioning]"
                "(https://semver.org/spec/v2.0.0.html).\n\n"
                "This file was automatically generated for "
                f"[incolumepy.utils](https://gitlab.com/development-incolume/"
                f"incolumepy.utils/-/tree/{__version__})\n"
                "\n---\n"
                f"## [0.2.0]\t &#8212; \t"
                f"{dt.datetime.now().strftime('%F')}:\n  - Fake record\n"
                f"## [0.1.1]\t &#8212; \t"
                f"{dt.datetime.now().strftime('%F')}:\n  - Fake record\n"
                f"## [0.1.1-rc.1]\t &#8212; \t"
                f"{dt.datetime.now().strftime('%F')}:\n  - Fake record\n"
                f"## [0.1.1-rc.0]\t &#8212; \t"
                f"{dt.datetime.now().strftime('%F')}:\n  - Fake record\n"
                f"## [0.1.1-alpha.0]\t &#8212; \t"
                f"{dt.datetime.now().strftime('%F')}:\n  - Fake record\n"
                f"## [0.1.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:"
                f"\n  - system\n"
                f"## [0.0.1]\t &#8212; \t"
                f"{dt.datetime.now().strftime('%F')}:\n  - Fake record\n"
                "---\n\n"
                "[0.1.1]: https://gitlab.com/development-incolume"
                "/incolumepy.utils/-/compare/0.1.0...0.1.1\n"
                "[0.1.1-alpha.0]: https://gitlab.com/"
                "development-incolume/incolumepy.utils/-"
                "/compare/0.1.1...0.1.1-alpha.0\n"
                "[0.1.1-rc.0]: https://gitlab.com/"
                "development-incolume/incolumepy.utils/-"
                "/compare/0.1.1-alpha.0...0.1.1-rc.0\n"
                "[0.1.1-rc.1]: https://gitlab.com/"
                "development-incolume/incolumepy.utils/-"
                "/compare/0.1.1-rc.0...0.1.1-rc.1\n"
                "[0.2.0]: https://gitlab.com/development-incolume/"
                "incolumepy.utils/-/compare/0.1.1-rc.1...0.2.0\n"
                "[0.0.1]: https://gitlab.com/development-incolume/"
                "incolumepy.utils/-/compare/0.2.0...0.0.1\n"
            ),
            # marks=pytest.mark.skip
        ),
        pytest.param(
            "0.1.0 system\n0.1.1 Fake record\n0.1.1-alpha.0 Fake record"
            "\n0.1.1-rc.0 Fake record\n0.1.1-rc.1 Fake record"
            "\n0.2.0 Fake record\n0.0.1 Fake record",
            False,
            (
                "# CHANGELOG\n\n\n"
                "All notable changes to this project "
                "will be documented in this file.\n\n"
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/),"
                " and this project adheres to [Semantic Versioning]"
                "(https://semver.org/spec/v2.0.0.html).\n\nThis file was "
                "automatically generated for "
                f"[incolumepy.utils](https://gitlab.com/development-incolume/"
                f"incolumepy.utils/-/tree/{__version__})\n"
                "\n---\n"
                f'## [0.0.1]\t &#8212; \t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                f'## [0.1.0]\t &#8212; \t{dt.datetime.now().strftime("%F")}:\n'
                "  - system\n"
                f"## [0.1.1-alpha.0]\t &#8212; "
                f'\t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                f"## [0.1.1-rc.0]\t &#8212; "
                f'\t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                f"## [0.1.1-rc.1]\t &#8212; "
                f'\t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                f'## [0.1.1]\t &#8212; \t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                f'## [0.2.0]\t &#8212; \t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                "---\n"
                "\n"
                "[0.1.1]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.1.0...0.1.1\n"
                "[0.1.1-alpha.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.1.1...0.1.1-alpha.0\n"
                "[0.1.1-rc.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.1.1-alpha.0...0.1.1-rc.0\n"
                "[0.1.1-rc.1]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.1.1-rc.0...0.1.1-rc.1\n"
                "[0.2.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.1.1-rc.1...0.2.0\n"
                "[0.0.1]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.2.0...0.0.1\n"
            ),
            # marks=pytest.mark.skip,
        ),
        pytest.param(
            "",
            False,
            (
                "# CHANGELOG\n\n\n"
                "All notable changes to this project "
                "will be documented in this file.\n\n"
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/), "
                "and this project adheres to [Semantic Versioning]"
                "(https://semver.org/spec/v2.0.0.html).\n\nThis file was "
                "automatically generated for "
                f"[incolumepy.utils](https://gitlab.com/development-incolume/"
                f"incolumepy.utils/-/tree/{__version__})\n"
                "\n"
                "---\n"
                "---\n"
                "\n"
            ),
            # marks=pytest.mark.skip,
        ),
        pytest.param(
            "",
            None,
            (
                "# CHANGELOG\n\n\n"
                "All notable changes to this project "
                "will be documented in this file.\n\n"
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/), "
                "and this project adheres "
                "to [Semantic Versioning]"
                "(https://semver.org/spec/v2.0.0.html).\n\nThis file was "
                "automatically generated for "
                f"[incolumepy.utils](https://gitlab.com/development-incolume/"
                f"incolumepy.utils/-/tree/{__version__})\n"
                "\n"
                "---\n"
                "---\n"
                "\n"
            ),
            # marks=pytest.mark.skip,
        ),
        pytest.param(
            "0.0.1 initial\nwip fake record\nWIP nihil"
            "\nquisquiliae fake\n0.1.0-alpha.0 dev fake\nv0.1.0 record",
            True,
            (
                "# CHANGELOG\n"
                "\n"
                "\n"
                "All notable changes to this project "
                "will be documented in this file.\n\n"
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/), "
                "and this project adheres to [Semantic Versioning]"
                "(https://semver.org/spec/v2.0.0.html).\n\nThis file was "
                "automatically generated for "
                f"[incolumepy.utils](https://gitlab.com/development-incolume/"
                f"incolumepy.utils/-/tree/{__version__})\n"
                "\n"
                "---\n"
                f"## [v0.1.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - record\n"
                f"## [0.1.0-alpha.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - dev fake\n"
                f"## [0.0.1]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - initial\n"
                "---\n"
                "\n"
                "[0.1.0-alpha.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.0.1...0.1.0-alpha.0\n"
                "[v0.1.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/0.1.0-alpha.0...v0.1.0\n"
            ),
            # marks=pytest.mark.skip,
        ),
        pytest.param(
            "v0.0.1 Added: initial"
            "\nv0.1.0 Added: record"
            "\nv0.1.0-alpha.0 Changed: dev fake"
            "\nv0.1.0-alpha.1 Deprecated: ass"
            "\nv0.0.1-rc.0 Fixed: as"
            "\nv0.0.1-alpha.0 Security: as"
            "\nv0.0.1-beta.0 Added: a"
            "\nv0.0.1-dev.0 Changed: asd"
            "\nv0.0.1-rc.1 as"
            "\nv0.0.1-rc.2 Fixed: as"
            "\nv0.0.1-rc.11 Changed: as"
            "\nv0.0.1-rc.3 Added: as"
            "\nv0.0.1-rc.12 Removed: as"
            "\nv0.0.1-rc.21 Deprecated: as\n",
            True,
            (
                "# CHANGELOG\n\n\n"
                "All notable changes to this project "
                "will be documented in this file.\n\n"
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/), "
                "and this project adheres to [Semantic Versioning]"
                "(https://semver.org/spec/v2.0.0.html).\n\nThis file was "
                "automatically generated for "
                f"[incolumepy.utils](https://gitlab.com/development-incolume/"
                f"incolumepy.utils/-/tree/{__version__})\n"
                "\n"
                "---\n"
                f"## [v0.1.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: record\n"
                f"## [v0.1.0-alpha.1]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Deprecated: ass\n"
                f"## [v0.1.0-alpha.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Changed: dev fake\n"
                f"## [v0.0.1]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: initial\n"
                f"## [v0.0.1-rc.21]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Deprecated: as\n"
                f"## [v0.0.1-rc.12]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Removed: as\n"
                f"## [v0.0.1-rc.11]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Changed: as\n"
                f"## [v0.0.1-rc.3]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: as\n"
                f"## [v0.0.1-rc.2]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Fixed: as\n"
                f"## [v0.0.1-rc.1]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - as\n"
                f"## [v0.0.1-rc.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Fixed: as\n"
                f"## [v0.0.1-alpha.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Security: as\n"
                f"## [v0.0.1-beta.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: a\n"
                f"## [v0.0.1-dev.0]\t &#8212; "
                f"\t{dt.datetime.now().strftime('%F')}:\n"
                "  - Changed: asd\n"
                "---\n"
                "\n"
                "[v0.1.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1...v0.1.0\n"
                "[v0.1.0-alpha.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.1.0...v0.1.0-alpha.0\n"
                "[v0.1.0-alpha.1]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.1.0-alpha.0...v0.1.0-alpha.1\n"
                "[v0.0.1-rc.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.1.0-alpha.1...v0.0.1-rc.0\n"
                "[v0.0.1-alpha.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-rc.0...v0.0.1-alpha.0\n"
                "[v0.0.1-beta.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-alpha.0...v0.0.1-beta.0\n"
                "[v0.0.1-dev.0]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-beta.0...v0.0.1-dev.0\n"
                "[v0.0.1-rc.1]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-dev.0...v0.0.1-rc.1\n"
                "[v0.0.1-rc.2]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-rc.1...v0.0.1-rc.2\n"
                "[v0.0.1-rc.11]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-rc.2...v0.0.1-rc.11\n"
                "[v0.0.1-rc.3]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-rc.11...v0.0.1-rc.3\n"
                "[v0.0.1-rc.12]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-rc.3...v0.0.1-rc.12\n"
                "[v0.0.1-rc.21]: "
                "https://gitlab.com/development-incolume/incolumepy.utils/-"
                "/compare/v0.0.1-rc.12...v0.0.1-rc.21\n"
            ),
            # marks=pytest.mark.skip,
        ),
    ],
)
def test_update_changelog(
    class_mocker, temp_file_name, str_testing, reverse, expected
):
    file = temp_file_name.with_suffix(".md")
    # print(file)
    entrance = {"changelog_file": file, "reverse": reverse}
    class_mocker.patch(
        "subprocess.getoutput",
        side_effect=[
            str_testing,
            *repeat(dt.datetime.now().strftime("%F"), 20),
        ],
    )
    update_changelog(**entrance)
    assert file.read_text() == expected


def test_update_changelog_deprecated(temp_file_name):
    with pytest.raises(
        expected_exception=NotImplementedError,
        match="This function was replaced. "
        "Use incolumepy.utils.changelog.update_changelog",
    ):
        update_changelog(changelog_file=temp_file_name)


@pytest.mark.parametrize(
    "entrance expected".split(),
    (
        ("incolumepy.package.module", ["incolumepy", "incolumepy.package"]),
        (
            "incolumepy.package.subpackage.module",
            [
                "incolumepy",
                "incolumepy.package",
                "incolumepy.package.subpackage",
            ],
        ),
        ("incolumepy.package.module", ["incolumepy", "incolumepy.package"]),
        ("incolumepy.package", ["incolumepy"]),
        ("incolumepy", ["incolumepy"]),
        (None, []),
    ),
)
def test_namespace(entrance, expected):
    assert namespace(entrance) == expected
    # if entrance:
    #     assert namespace(entrance) == expected
    # else:
    #     with pytest.raises(expected_exception=ValueError, match=""):
    #         namespace(entrance)


def test_logger(temp_file_name):
    logg = logger(filelog=temp_file_name)
    assert isinstance(logg, logging.Logger)


# def test_logger(caplog, temp_file_name):
#    l = logger(filelog=temp_file_name)
#    l.debug('debug')
#    l.info('info')
#    l.error('error')
#    l.warn('warn')
#    assert temp_file_name.exists()
#
#
# def test_func(temp_file_name, caplog):
#    LOGGER = logger(filelog=temp_file_name)
#    LOGGER.debug('Testing now.')
#    assert 'Testing now.' in caplog.text
#
#
# class SpamTest:
#    @pytest.fixture(autouse=True)
#    def inject_fixtures(self, caplog):
#        self._caplog = caplog
#
#    def test_eggs(self, temp_file_name):
#        LOGGER = logger(filelog=temp_file_name)
#        with self._caplog.at_level(logging.INFO):
#            LOGGER.info('info bacon')
#            assert self._caplog.records[0].message == 'bacon'
