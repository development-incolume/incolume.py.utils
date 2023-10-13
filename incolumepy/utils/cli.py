"""Command Line Interface module."""
import codecs
import logging
import sys
from pathlib import Path
from typing import Union

import click

from incolumepy.utils.changelog import update_changelog


@click.command()
@click.argument("nome", envvar="USER", type=click.STRING)
def greeting(nome):
    """Retorna o cumprimento para o nome passado.

    :param nome: str
    :return: None
    """
    click.echo(f"Oi {nome}!")


@click.command()
@click.option("--shout", is_flag=True)
def info(shout):
    """Enhancement for example click simple flag."""
    rv = sys.platform
    if shout:
        rv = rv.upper() + "!!!!"
    click.echo(rv)


@click.command()
@click.option("--shout/--no-shout", default=False)
def info1(shout):
    """Enhancement for example click double flag."""
    rv = sys.platform
    if shout:
        rv = rv.upper() + "!!!!"
    click.echo(rv)


@click.command()
@click.option("--shout/--no-shout", " /-S", default=False)
def info2(shout):
    """Enhancement for example click triple flag."""
    rv = sys.platform
    if shout:
        rv = rv.upper() + "!!!!"
    click.echo(rv)


@click.command()
@click.option("--upper", "transformation", flag_value="upper", default=True)
@click.option("--lower", "transformation", flag_value="casefold")
@click.option("--capitalize", "transformation", flag_value="capitalize")
def info3(transformation):
    """Enhancement for example click flag_value."""
    click.echo(getattr(sys.platform, transformation)())


@click.command()
@click.option(
    "--hash-type", type=click.Choice(["MD5", "SHA1"], case_sensitive=False)
)
def digest(hash_type):
    """Enhancement for example click choices."""
    click.echo(hash_type)


@click.command()
@click.option(
    "--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True
)
def encode(password):
    """Encode password with rot13."""
    click.echo(f"encoded: {codecs.encode(password, 'rot13')}")


@click.command()
# @click.argument('stream', type=click.STRING)
@click.argument("file_changelog", type=click.STRING, default="CHANGELOG.md")
@click.option(
    "--url",
    "-u",
    default=(
        "https://gitlab.com/development-incolume/incolumepy.utils/-/compare"
    ),
    help="Url compare from repository of project.",
)
@click.option(
    "--reverse",
    "-r",
    default=True,
    is_flag=True,
    help="Reverse order of records.",
)
@click.option(
    "--with_prereleases",
    "-p",
    default=True,
    is_flag=True,
    help="Include prereleases of records.",
)
def changelog(
    file_changelog: Union[Path, str],
    url: str = "",
    reverse: bool = True,
    with_prereleases: bool = True,
):
    """Operacionaliza uma interface CLI para módulo incolumepy.utils.changelog.

    :param file_changelog: changelog full filename.
    :param url: url compare from repository of project.
    :param reverse: bool.
    :param with_prereleases: bool. If include prereleases of records.
    :return: bool. True if success

    """
    logging.debug("file_changelog: %s", file_changelog)
    logging.debug("url: %s", url)
    logging.debug("reverse: %s", reverse)
    logging.debug("with_prereleases: %s", with_prereleases)

    result = update_changelog(
        changelog_file=file_changelog,
        urlcompare=url,
        reverse=bool(reverse),
        with_prereleases=bool(with_prereleases),
    )
    return result
