import click
from incolumepy.utils.changelog import update_changelog

@click.command()
@click.argument('nome', envvar='USER', type=click.STRING)
def greeting(nome):
    click.echo(f'Oi {nome}!')

@click.command()
# @click.argument('stream', type=click.STRING)
@click.argument('file_changelog', type=click.STRING, default='CHANGELOG.md')
def changelog(file_changelog):

