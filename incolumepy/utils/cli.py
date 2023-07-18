import click

@click.command()
@click.argument('nome')
def changelog(nome):
    click.echo(f'Oi {nome}!')


changelog()
