import click
from incolumepy.utils import changelog

@click.command()
@click.argument('nome', envvar='USER', type=click.STRING)
def changelog(nome):
    click.echo(f'Oi {nome}!')


changelog()
