import pytest

from incolumepy.utils.url import check_url

__author__ = "@britodfbr"  # pragma: no cover


class TestUtilURL:
    @pytest.mark.parametrize(
        "entrance expected".split(),
        [
            ("http://www.example.com", True),
            ("example.com", False),
            ("https://localhost", True),
            ("https://localhost:8080", True),
            ("127.0.0.1", False),
            ("http://127.0.0.1", True),
            ("http://127.0.0.1:3141", True),
        ],
    )
    def test_check_url(self, entrance, expected):
        assert check_url(entrance) == expected
