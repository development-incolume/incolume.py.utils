"""Changelog Module."""

import inspect
import logging
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Tuple

from incolumepy.utils import __title__, __version__, key_versions_2_sort

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)

CHANGELOG_FILE = Path(__file__).parents[2] / "CHANGELOG.md"


def msg_classify(msg: str) -> Dict[str, Any]:
    """
    Classify and sort one record for messages git tag.

    :param msg: str
    :return: dict
    """
    key, msg = msg.split(maxsplit=1)
    date = subprocess.getoutput(
        "git show -s --format=%%cs %s^{commit}" % key  # pylint: disable=C0209
    )
    logging.debug("key=%s; date=%s; msg=%s", key, date, msg)
    txt = re.sub(
        "(Added|Changed|Deprecated|Removed|Fixed|Security):",
        r"§§\1§:",
        msg,
        flags=re.I,
    )
    logging.debug("txt=%s", txt)
    dct: Dict[str, Any] = {}
    for i, j in sorted(
        x.strip().rstrip(";").split("§:") for x in txt.strip().split("§§") if x
    ):
        dct.setdefault(i.capitalize(),[]).extend(j.strip().split(";"))

    result = {"key": key, "date": date, "messages": dct}
    return result


def changelog_messages(
    *, text: str, start: Any = None, end: Any = None
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Changelog messages sort and classify.

    :param text: str
    :param start: (int, str, None)
    :param end: (int, str, None)
    :return: list
    """
    records = []
    for msg in text.strip().splitlines()[start:end]:
        logging.debug("msg=%s", msg)
        record = msg_classify(msg)
        logging.debug("record=%s", record)
        # records.setdefault(record['key']).update(**record)
        records.append((record["key"], record))
    logging.debug("type return %s=%s", inspect.stack()[0][3], type(records))
    logging.debug("return %s=%s", inspect.stack()[0][3], records)
    return records


def changelog_header() -> List[str]:
    """Header of changelog file."""
    content_formated = [
        "# CHANGELOG\n\n\n",
        "All notable changes to this project",
        " will be documented in this file.\n\n",
        "The format is based on ",
        "[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), ",
        "this project adheres to "
        "[Semantic Versioning](https://semver.org/spec/v2.0.0.html) "
        "and [Conventional Commit]"
        "(https://www.conventionalcommits.org/pt-br/v1.0.0/).\n\n",
        "This file was automatically generated for",
        f" [{__title__}](https://gitlab.com/development-incolume/"
        f"incolumepy.utils/-/tree/{__version__})",
        "\n\n---\n",
    ]
    return content_formated


def changelog_body(
    content: List[Tuple[str, Dict[str, Any]]],
    content_formated: List[str],
    **kwargs,
) -> List[str]:
    """Body of changelog file."""
    for _, entrada in content:
        logging.debug(entrada)
        content_formated.append(
            f"\n\n## [{entrada['key']}]\t &#8212; \t{entrada['date']}:"
        )
        for label, msgs in entrada["messages"].items():
            content_formated.append(f"\n### {label.capitalize()}")
            for msg in msgs:
                content_formated.append(f"\n  - {msg.strip()}")
    return content_formated


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
                f'[{x["key"]}]: {urlcompare}/{y["key"]}...{x["key"]}\n'
            )
        y = x
    return content_formated


def changelog_write(
    *, content: List[Tuple[str, Dict[str, Any]]], **kwargs
) -> bool:
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
    :return: bool. True if success

    >>> update_changelog()
    True
    >>> update_changelog(changelog_file='/tmp/CHANGELOG.md')
    True
    >>> update_changelog(changelog_file=Path('CHANGELOG.md'),
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
            ),
            reverse=reverse,
            key=key_versions_2_sort,
        ),
        urlcompare=urlcompare,
        changelog_file=changelog_file,
    )


class Changelog:
    """Changelog class."""


def run():
    """Examples ran.

    :return: None
    """
    msg = subprocess.getoutput("git tag -n").splitlines()[-14]
    logging.debug(msg)
    logging.debug("msg_classify=%s", msg_classify(msg=msg))

    msg = subprocess.getoutput("git tag -n")
    result = changelog_messages(text=msg)

    logging.debug("result=%s", result)
    logging.debug("type(result)=%s", type(result))
    result = sorted(result, reverse=True, key=key_versions_2_sort)
    logging.debug("result = %s; result type = %s", result, type(result))

    changelog_write(content=result)
    update_changelog()


if __name__ == "__main__":  # pragma: no cover
    run()
