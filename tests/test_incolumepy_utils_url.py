import re

import pytest

from incolume.py.utils.url import check_url, identify_dom_url

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
            (
                "http://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm",
                True,
            ),
            (
                "https://www2.camara.leg.br/legin/fed/declei/1940-1949"
                "/decreto-lei-2848-7-dezembro-1940-412868-"
                "publicacaooriginal-1-pe.html",
                True,
            ),
            (
                "https://legis.senado.leg.br/norma/527942/publicacao/15636360",
                True,
            ),
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

    @pytest.mark.parametrize(
        "entrance expected".split(),
        [
            (
                {
                    "url": "https://www2.camara.leg.br/legin/fed/carreg_sn"
                    "/anterioresa1824/cartaregia-39331-10-julho-1818"
                    "-569289-publicacaooriginal-92518-pe.html",
                },
                "camara",
            ),
            (
                {
                    "url": "https://www.planalto.gov.br/ccivil_03"
                    "/leis/lim/lim-26-8-1826.htm",
                },
                "planalto",
            ),
            (
                {
                    "url": "https://www.presidencia.gov.br/ccivil_03"
                    "/leis/lim/lim-26-8-1826.htm",
                    "lista_dominio": ["presidencia", "planalto"],
                },
                "presidencia",
            ),
            (
                {
                    "url": "http://legis.senado.leg.br/norma/416863"
                    "/publicacao/15637291",
                },
                "senado",
            ),
            (
                {
                    "url": "https://www.google.com.br",
                },
                "",
            ),
            (
                {
                    "url": "https://www.google.com.br",
                    "lista_dominio": ["google"],
                },
                "google",
            ),
            (
                {
                    "url": "https://google.com",
                    "lista_dominio": ["planalto", "camara", "senado"],
                },
                "",
            ),
            (
                {
                    "url": "https://google.com",
                    "lista_dominio": [
                        "google",
                        "planalto",
                        "camara",
                        "senado",
                    ],
                },
                "google",
            ),
        ],
    )
    def test_identify_dom_url_return(self, entrance, expected):
        assert identify_dom_url(**entrance) == expected

    @pytest.mark.parametrize(
        "entrance expected".split(),
        [
            ({"url": "https://google.com", "verboso": True}, ""),
            (
                {
                    "url": "https://google.com",
                    "lista_dominio": ["google"],
                    "verboso": True,
                },
                "google",
            ),
            (
                {
                    "url": "https://www.planalto.gov.br/ccivil_03/leis/"
                    "lim/lim-26-8-1826.htm",
                    "lista_dominio": ["planalto"],
                    "verboso": True,
                },
                "planalto",
            ),
            (
                {
                    "url": "https://www.planalto.gov.br/ccivil_03/leis/"
                    "lim/lim-26-8-1826.htm",
                    "lista_dominio": ["incolume"],
                    "verboso": True,
                },
                "",
            ),
            (
                {
                    "url": "https://blog.incolume.com.br",
                    "lista_dominio": ["incolume"],
                    "verboso": True,
                },
                "incolume",
            ),
        ],
    )
    def test_identify_dom_url_verbose(self, entrance, expected, capfd):
        assert identify_dom_url(**entrance) == expected
        out, err = capfd.readouterr()
        assert err == ""
        assert re.compile(r".*url.*(?:lista_dominio|verboso).*").search(out)
