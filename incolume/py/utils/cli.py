"""Command Line Interface module."""

import codecs
import sys

import click


@click.command()
@click.argument('nome', envvar='USER', type=click.STRING)
def greeting(nome):
    """Retorna o cumprimento para o nome passado.

    :param nome: str
    :return: None
    """
    click.echo(f'Oi {nome}!')


@click.command()
@click.option('--shout', is_flag=True)
def info(shout):
    """Enhancement for example click simple flag."""
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!'
    click.echo(rv)


@click.command()
@click.option('--shout/--no-shout', default=False)
def info1(shout):
    """Enhancement for example click double flag."""
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!'
    click.echo(rv)


@click.command()
@click.option('--shout/--no-shout', ' /-S', default=False)
def info2(shout):
    """Enhancement for example click triple flag."""
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!'
    click.echo(rv)


@click.command()
@click.option('--upper', 'transformation', flag_value='upper', default=True)
@click.option('--lower', 'transformation', flag_value='casefold')
@click.option('--capitalize', 'transformation', flag_value='capitalize')
def info3(transformation):
    """Enhancement for example click flag_value."""
    click.echo(getattr(sys.platform, transformation)())


@click.command()
@click.option(
    '--hash-type',
    type=click.Choice(['MD5', 'SHA1'], case_sensitive=False),
)
def digest(hash_type):
    """Enhancement for example click choices."""
    click.echo(hash_type)


@click.command()
@click.option(
    '--password',
    '-p',
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
)
def encode(password):
    """Encode password with rot13."""
    click.echo(f'encoded: {codecs.encode(password, "rot13")}')
