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
            ("http://www.example.com", True),
            ("example.com", False),
            ("https://localhost", True),
            ("https://localhost:8080", True),
            ("127.0.0.1", False),
            ("http://127.0.0.1", True),
            ("http://127.0.0.1:80", True),
            ("http://127.0.0.1:3141", True),
            ("https://presidencia.gov.br/CCIVIL_03/", True),
            ("https://planalto.gov.br/CCIVIL_03/", True),
            ("https://www.planalto.gov.br/CCIVIL_03/", True),
            ("http://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm", True),
            ("https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-"
             "dezembro-1940-412868-publicacaooriginal-1-pe.html",
             True,
             ),
            ("https://legis.senado.leg.br/norma/527942/publicacao/15636360", True),
            ("https://www.google.com.br", True),
            ("https://www.google.com", True),
            ("http://www.google.com", True),
            ("http://google.com", True),
            ("google.com", False),
            ("https://bb.b.br", True),
        ],
    )
    def test_check_url(self, entrance, expected):
        assert check_url(entrance) == expected
