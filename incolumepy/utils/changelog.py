import logging
import re
import subprocess
from pathlib import Path
from types import NoneType
from typing import Any, List, Dict

from incolumepy.utils import __version__, __title__, key_versions_2_sort


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)


def msg_classify(msg: str) -> dict:
    key, msg = msg.split(maxsplit=1)
    date = subprocess.getoutput(
        r"git show -s --format=%%cs %s^{commit}" % key
    )
    logging.debug(f"{key=}; {date=}; {msg=}")
    txt = re.sub(
        "(Added|Changed|Deprecated|Removed|Fixed|Security):",
        r"§\1:",
        msg,
        flags=re.I
    )
    dct = {}
    for i, j in (
        x.rstrip().rstrip(';').split(':')
        for x in txt.strip().split('§') if x
    ):
        dct.setdefault(i, []).extend(j.strip().split(';'))

    result = {'key': key, 'date': date, 'messages': dct}
    return result


def changelog_messages(
        *, text: str, start: Any = None, end: Any = None) -> list:
    records = []
    for msg in text.strip().splitlines()[start:end]:
        logging.debug(f"{msg=}")
        record = msg_classify(msg)
        logging.debug(f"{record=}")
        # records.setdefault(record['key']).update(**record)
        records.append((record['key'], record))
    logging.debug(f"{type(records)}")
    return records


def changelog_write(**kwargs):
    changelog_file = kwargs.get('changelog_file') \
                     or Path(__file__).parents[2] / 'CHANGELOG.md'
    content = kwargs.get('content')
    urlcompare = (
        kwargs.get('urlcompare')
        or "https://gitlab.com/development-incolume/incolumepy.utils/-/compare"
    )
    with changelog_file.open("w") as f:
        f.writelines(
            ["# CHANGELOG\n\n\n",
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
        )
        for _, entrada in content:
            logging.debug(entrada)
            f.write(f"\n\n## [{entrada['key']}]\t &#8212; \t{entrada['date']}:")
            for label, msgs in entrada['messages'].items():
                f.write(f"\n### {label}")
                for msg in msgs:
                    f.write(f"\n  - {msg}")

        f.write("\n---\n\n")
        y = {}
        for _, x in content[::-1]:
            if y:
                f.write(
                    f'[{x["key"]}]: {urlcompare}/{y["key"]}...{x["key"]}\n'
                )
            y = x
    return True


def update_changelog(**kwargs):
    """
    Update Changelog.md file.

    :param urlcompare: url compare from repository of project.
    :param reverse: bool.
    :param changelog_file:  changelog full filename.
    :return:
    """
    logging.debug(kwargs)
    changelog_file = kwargs.get('changelog_file')
    if isinstance(changelog_file, Path):
        pass
    elif isinstance(changelog_file, str):
        changelog_file = Path(kwargs.get('changelog_file'))
    elif isinstance(changelog_file, NoneType):
        changelog_file = Path(__file__).parents[2] / 'CHANGELOG.md'
    logging.debug(f'{changelog_file=}')

    reverse = (
        kwargs.get('reverse')
        if isinstance(kwargs.get('reverse'), bool)
        else True
    )
    urlcompare = (
        kwargs.get('urlcompare')
        or "https://gitlab.com/development-incolume/incolumepy.utils/-/compare"
    )
    conteudo = subprocess.getoutput("git tag -n")
    logging.info("registros encontrados ..")
    logging.debug(f"{conteudo=}")

    return changelog_write(
        content=sorted(
            changelog_messages(
                text=conteudo,
                start=kwargs.get('start', None),
                end=kwargs.get('end', None)
            ),
            reverse=reverse,
            key=key_versions_2_sort,
        ),
        urlcompare=urlcompare,
        changelog_file=changelog_file,
    )


class Changelog:
    ...


def run():
    msg = subprocess.getoutput('git tag -n').splitlines()[-14]
    logging.debug(msg)
    logging.debug(msg_classify(msg=msg))

    msg = subprocess.getoutput('git tag -n')
    result = changelog_messages(text=msg)

    logging.debug(f"{result=}")
    logging.debug(f"{type(result)=}")
    result = sorted(result, reverse=True, key=key_versions_2_sort)
    logging.debug(f"{result=}")

    changelog_write(content=result)
    update_changelog()


if __name__ == '__main__':    # pragma: no cover
    run()
