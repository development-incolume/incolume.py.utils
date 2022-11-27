"""Utils tests."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import re
from collections import OrderedDict
from itertools import repeat

import pytest

from incolumepy.utils import (
    __version__,
    confproject,
    key_versions_2_sort,
    update_changelog,
    versionfile,
)

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
    ["entrance", "expected"],
    (
        (__version__, True),
        ("0.0.1", True),
        ("0.1.0", True),
        ("1.0.0", True),
        ("1.0.1", True),
        ("1.1.1", True),
        ("1.1.1-rc0", True),
        ("1.1.1-rc.0", True),
        ("1.1.1-rc-0", True),
        ("1.0.1-dev0", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-dev.1", True),
        ("1.0.1-dev.2", True),
        ("1.0.1-alpha.0", True),
        ("1.0.1-alpha.266", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-beta.0", True),
        ("1.1.1-alpha.99999", True),
        ("1.1.1-rc.99999", True),
        ("1.1.99999", True),
        ("1.999999.1", True),
    ),
)
def test_version(entrance, expected):
    assert re.fullmatch(r"\d\.\d\.\d(-\w+\.\d+)?", __version__, flags=re.I)


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
        (("0.5.1-rc.9", "aaa"), "00000501.030009"),
        (("0.5.1-rc1", "aaa"), "00000501.030001"),
        (("0.5.1-alpha.1", "aaa"), "00000501.020001"),
        (("0.5.1-alpha.2", "aaa"), "00000501.020002"),
        (("0.5.1-alpha.3", "aaa"), "00000501.020003"),
        (("0.5.1-alpha.4", "aaa"), "00000501.020004"),
        (("0.5.1-alpha.0", "aaa"), "00000501.020000"),
        (("0.5.1-post.0", "aaa"), "00000501.400000"),
        (("1.5.1-post0", "aaa"), "00010501.400000"),
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
                f"## [0.1.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n  - system\n"
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
                f'## [0.1.1-alpha.0]\t &#8212; \t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                f'## [0.1.1-rc.0]\t &#8212; \t{dt.datetime.now().strftime("%F")}:\n'
                "  - Fake record\n"
                f'## [0.1.1-rc.1]\t &#8212; \t{dt.datetime.now().strftime("%F")}:\n'
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
                f"## [v0.1.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - record\n"
                f"## [0.1.0-alpha.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
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
                f"## [v0.1.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: record\n"
                f"## [v0.1.0-alpha.1]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Deprecated: ass\n"
                f"## [v0.1.0-alpha.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Changed: dev fake\n"
                f"## [v0.0.1]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: initial\n"
                f"## [v0.0.1-rc.21]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Deprecated: as\n"
                f"## [v0.0.1-rc.12]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Removed: as\n"
                f"## [v0.0.1-rc.11]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Changed: as\n"
                f"## [v0.0.1-rc.3]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: as\n"
                f"## [v0.0.1-rc.2]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Fixed: as\n"
                f"## [v0.0.1-rc.1]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - as\n"
                f"## [v0.0.1-rc.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Fixed: as\n"
                f"## [v0.0.1-alpha.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Security: as\n"
                f"## [v0.0.1-beta.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
                "  - Added: a\n"
                f"## [v0.0.1-dev.0]\t &#8212; \t{dt.datetime.now().strftime('%F')}:\n"
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
