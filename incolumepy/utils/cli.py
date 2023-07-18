"""Command Line Interface module."""

from pathlib import Path

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
# @click.argument('stream', type=click.STRING)
@click.argument("file_changelog", type=click.STRING, default="CHANGELOG.md")
def changelog(file_changelog: str | Path):
    """Operacionaliza uma interface CLI para módulo incolumepy.utils.changelog.

    :param changelog_file:  changelog full filename.
    :return: bool. True if success

    """
    return update_changelog(changelog_file=file_changelog)
