"""Changelog Module."""

import inspect
import logging
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from deprecated import deprecated

from incolume.py.utils import __title__, __version__
from incolume.py.utils.tools import key_versions_2_sort

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;%(module)s;%(funcName)s;%(message)s",
)

CHANGELOG_FILE = Path(__file__).parents[2] / "CHANGELOG.md"


def msg_classify(msg: str, lang: str = "", **kwargs) -> Dict[str, Any]:
    """
    Classify and sort one record for messages git tag -n.

    :param lang:
    :param msg: str
    :param with_prereleases: bool. If include prereleases of records.
    :return: dict
    :exception ValueError for unsuported lang
    :exception ReferenceError for msg not due keepachangelog.
    """
    with_prereleases = kwargs.get("with_prereleases", False)
    logging.debug(msg)
    logging.debug(lang)
    logging.debug(with_prereleases)
    suport_lang: Dict[Any, Any] = {
        "en-US": {
            "Added": "Added",
            "Changed": "Changed",
            "Deprecated": "Deprecated",
            "Removed": "Removed",
            "Fixed": "Fixed",
            "Security": "Security",
        },
        "pt-BR": {
            "Adicionado": "Added",
            "Modificado": "Changed",
            "Obsoleto": "Deprecated",
            "Removido": "Removed",
            "Corrigido": "Fixed",
            "Segurança": "Security",
        },
    }
    suport_lang.update(
        {"all": {k: v for d in suport_lang.values() for k, v in d.items()}}
    )
    lang = lang or "all"
    logging.debug("lang=%s", lang)

    if lang not in suport_lang:
        logging.error(ValueError(f"{lang} not suported! Use {suport_lang.keys()}"))

    key, msg = msg.split(maxsplit=1)

    date = subprocess.getoutput(
        'git show -s --pretty="%%cs" %s^{commit} --' % key  # pylint: disable=C0209
    )
    logging.debug("key=%s; date=%s; msg=%s", key, date, msg)
    selected_lang = suport_lang.get(lang, suport_lang["all"])
    # regex = "(Added|Changed|Deprecated|Removed|Fixed|Security):"
    regex: str = rf"({'|'.join(selected_lang.keys())})\s?:"
    txt = re.sub(
        regex,
        r"§§\1§:",
        msg,
        flags=re.I,
    )
    logging.debug("txt=%s", txt)
    dct: Dict[str, Any] = {}
    try:
        for i, j in sorted(
            x.strip().rstrip(";").split("§:") for x in txt.strip().split("§§") if x
        ):
            dct.setdefault(selected_lang[i.capitalize()], []).extend(
                j.strip().split(";")
            )
    except ValueError as e:
        logging.error("%s: %s", e.__class__.__name__, e)
        # if re.match("not enough values to unpack", str(e), re.I):
        raise ReferenceError(
            f"The tag entry '{key}' was rejected due for not to "
            f"follow the 'keep a changelog' default partner."
        ) from e
    result = {"key": key, "date": date, "messages": dct}
    return result


def changelog_messages(
    *, text: str, start: Any = None, end: Any = None, **kwargs
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Changelog messages sort and classify.

    :param text: str
    :param start: (int, str, None)
    :param end: (int, str, None)
    :param with_prereleases: bool. If include prereleases of records.
    :return: list
    """
    logging.debug("parameters: (%s %s %s %s)", text, start, end, kwargs)
    lang = kwargs.get("lang", "")
    with_prereleases = kwargs.get("with_prereleases", True)
    r1 = r"Unreleased|\d+(\.\d+){2}(-?\w+\.?\d+)?"
    r2 = r"Unreleased|\d+(\.\d+){2}"
    records = []
    for msg in text.strip().splitlines()[start:end]:
        logging.debug("msg=%s", msg)
        try:
            record = msg_classify(msg=msg, lang=lang)
            logging.debug("record=%s", record)

            key = record["key"]
            logging.debug("key=%s", key)

            # records.setdefault(record['key']).update(**record)
            if (with_prereleases and re.fullmatch(r1, key, re.I)) or (
                not with_prereleases and re.fullmatch(r2, key, re.I)
            ):
                records.append((key, record))
            else:
                pass

        except (ValueError, ReferenceError) as err:
            logging.error("%s: %s", err.__class__.__name__, err)

    logging.debug("type return %s=%s", inspect.stack()[0][3], type(records))
    logging.debug("return %s=%s", inspect.stack()[0][3], records)
    return records


@deprecated(
    reason="This function is outdated, use `Changelog.header` instead."
    " It will be discontinued in the near future.",
    version="1.11.0",
)
def changelog_header(
    url_keepachangelog: str = "",
    url_semver: str = "",
    url_convetional_commit: str = "",
    **kwargs,
) -> List[str]:
    """Header of changelog file."""
    url_keepachangelog = url_keepachangelog or "https://keepachangelog.com/en/1.0.0/"
    url_semver = url_semver or "https://semver.org/spec/v2.0.0.html"
    url_convetional_commit = (
        url_convetional_commit or "https://www.conventionalcommits.org/pt-br/v1.0.0/"
    )
    # content_formated = [
    #     "# CHANGELOG\n\n\n",
    #     "All notable changes to this project",
    #     " will be documented in this file.\n\n",
    #     "The format is based on ",
    #     f"[Keep a Changelog]({url_keepachangelog}), ",
    #     "this project adheres to "
    #     f"[Semantic Versioning]({url_semver}) "
    #     f"and [Conventional Commit]({url_convetional_commit}).\n\n",
    #     "This file was automatically generated for",
    #     f" [{__title__}](https://gitlab.com/development-incolume/"
    #     f"incolumepy.utils/-/tree/{__version__})",
    #     "\n\n---\n",
    # ]
    # return content_formated
    obj = Changelog(
        url_semver=url_semver,
        url_keepachangelog=url_keepachangelog,
        url_convetional_commit=url_convetional_commit,
        url_pricipal=("https://gitlab.com/development-incolume/incolumepy.utils"),
        **kwargs,
    )
    return obj.header()


def changelog_body(
    content: List[Tuple[str, Dict[str, Any]]],
    content_formated: List[str],
    **kwargs,
) -> List[str]:
    """Body of changelog file."""
    content_formated.extend(Changelog.iter_logs(content[:-1]))
    content_formated.extend(Changelog.iter_logs(content[-1:], False))
    return content_formated


@deprecated(
    reason="This function is outdated, use `Changelog.header` instead."
    " It will be discontinued in the near future.",
    version="1.11.0",
)
def changelog_footer(
    content: List[Tuple[str, Dict[str, Any]]],
    content_formated: List[str],
    **kwargs,
) -> List[str]:
    """Footer of changelog file."""
    urlcompare = (
        kwargs.get("urlcompare")
        or "https://gitlab.com/development-incolume/incolumepy.utils/-/compare"
    )
    logging.debug("urlcompare=%s", urlcompare)
    content_formated.append("\n---\n\n")
    y: Dict[str, Any] = {}
    for _, x in content[::-1]:
        if y:
            content_formated.append(
                f"[{x['key']}]: {urlcompare}/{y['key']}...{x['key']}\n"
            )
        y = x
    return content_formated


def changelog_write(*, content: List[Tuple[str, Dict[str, Any]]], **kwargs) -> bool:
    """Write CHANGELOG.md file formatted.

    :param content: List[Tuple[str, Dict[str, Any]]]
    :param changelog_file: str, pathlib
    :param urlcompare: str
    :return: bool. True if success.
    """
    changelog_file = Path(kwargs.get("changelog_file") or CHANGELOG_FILE)
    logging.debug("changelog_file=%s", changelog_file)

    content_formated = changelog_header()
    content_formated = changelog_body(content, content_formated, **kwargs)
    content_formated = changelog_footer(content, content_formated, **kwargs)

    with changelog_file.open("w") as f:
        f.writelines(content_formated)
        return True


def update_changelog(
    *,
    changelog_file: Any = None,
    reverse: bool = True,
    **kwargs,
):
    """
    Update Changelog.md file.

    :param urlcompare: url compare from repository of project.
    :param reverse: bool.
    :param changelog_file:  changelog full filename.
    :param with_prereleases: bool. If include prereleases of records.
    :return: bool. True if success

    >> update_changelog()
    True
    >> update_changelog(changelog_file='/tmp/CHANGELOG.md')
    True
    >> update_changelog(
    changelog_file=Path('CHANGELOG.md'),
    urlcompare="https://gitlab.com/development-incolume
    /incolumepy.utils/-/compare")
    True
    """
    logging.debug("argumentos=%s,%s,%s", changelog_file, reverse, kwargs)
    # if isinstance(changelog_file, str):
    #     changelog_file = Path(changelog_file)
    # elif isinstance(changelog_file, type(None)):
    #     changelog_file = CHANGELOG_FILE

    urlcompare: str = (
        kwargs.get("urlcompare")
        or "https://gitlab.com/development-incolume/incolumepy.utils/-/compare"
    )
    content: str = kwargs.get("content", subprocess.getoutput("git tag -n"))
    logging.info("registros encontrados ..")
    logging.debug("content=%s", content)

    return changelog_write(
        content=sorted(
            changelog_messages(
                text=content,
                start=kwargs.get("start", None),
                end=kwargs.get("end", None),
                with_prereleases=kwargs.get("with_prereleases", False),
            ),
            reverse=reverse,
            key=key_versions_2_sort,
        ),
        urlcompare=urlcompare,
        changelog_file=changelog_file,
    )


class Changelog:
    """Changelog class."""

    def __init__(
        self,
        *,
        file_output: Union[Path, str] = "",
        url_compare: str = "",
        reverse: bool = True,
        **kwargs,
    ):
        """Initialize from Changelog class."""
        self.file_output = file_output or Path("CHANGELOG.md")
        self.url_compare = (
            url_compare
            or "https://gitlab.com/development-incolume/incolumepy.utils/-/compare"
        )
        self.reverse = reverse
        self.url_principal = kwargs.get(
            "url_pricipal",
            "https://gitlab.com/development-incolume/incolumepy.utils",
        )
        self.url_keepachangelog = kwargs.get(
            "url_keepachangelog", "https://keepachangelog.com/en/1.0.0/"
        )
        self.url_semver = kwargs.get(
            "url_semver", "https://semver.org/spec/v2.0.0.html"
        )
        self.url_convetional_commit = kwargs.get(
            "url_convetional_commit",
            "https://www.conventionalcommits.org/pt-br/v1.0.0/",
        )

    # @property
    # def url_compare(self):
    #     return f'{self.url_principal}/-/tree/{__version__}'

    @staticmethod
    def iter_logs(
        content: List[Tuple[str, Dict[str, Any]]], linked: bool = True
    ) -> List[str]:
        """Iterador de registros git."""
        result = []
        for _, entrada in content:
            logging.debug(entrada)
            if linked:
                result.append(
                    f"\n\n## [{entrada['key']}]\t &#8212; \t{entrada['date']}:"
                )
            else:
                result.append(f"\n\n## {entrada['key']}\t &#8212; \t{entrada['date']}:")

            for label, msgs in entrada["messages"].items():
                result.append(f"\n### {label.capitalize()}")
                for msg in msgs:
                    frase = msg.strip()
                    frase = frase[0].upper() + frase[1:]
                    result.append(f"\n  - {frase};")
        return result

    def header(self) -> List[str]:
        """Header of changelog file."""
        content_formated = [
            "# CHANGELOG\n\n\n",
            "All notable changes to this project",
            " will be documented in this file.\n\n",
            "The format is based on ",
            f"[Keep a Changelog]({self.url_keepachangelog}), ",
            "this project adheres to "
            f"[Semantic Versioning]({self.url_semver}) "
            f"and [Conventional Commit]({self.url_convetional_commit}).\n\n",
            "This file was automatically generated for",
            f" [{__title__}]({self.url_principal}/-/tree/{__version__})",
            "\n\n---\n",
        ]
        return content_formated

    def footer(self, **kwargs) -> List[str]:
        """Footer of changelog file."""
        content: List[Tuple[str, Dict[str, Any]]] = kwargs.get("content") or []
        content_formated: List[str] = kwargs.get("content_formated") or []
        url_compare = kwargs.get("url_compare") or self.url_compare

        logging.debug("url_compare=%s", url_compare)

        content_formated.append("\n---\n\n")
        y: Dict[str, Any] = {}
        for _, x in content[::-1]:
            if y:
                content_formated.append(
                    f"[{x['key']}]: {url_compare}/{y['key']}...{x['key']}\n"
                )
            y = x
        return content_formated


def run():
    """Examples ran.

    :return: None
    """
    msg = subprocess.getoutput("git tag -n").splitlines()[-14]
    logging.debug(msg)
    logging.debug("msg_classify=%s", msg_classify(msg=msg))

    # msg = subprocess.getoutput("git tag -n")
    result = changelog_messages(text=msg)

    logging.debug("result=%s", result)
    logging.debug("type(result)=%s", type(result))
    result = sorted(result, reverse=True, key=key_versions_2_sort)
    logging.debug("result = %s; result type = %s", result, type(result))

    changelog_write(content=result)
    update_changelog()


if __name__ == "__main__":  # pragma: no cover
    run()
