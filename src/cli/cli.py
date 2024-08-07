import click

from src.core.MinBit import MinBit


@click.group()
def cli():
    pass

@click.command()
def wallet():
    MinBit().make_wallet("alias", "address", "pass")

cli.add_command(wallet)

if __name__ == '__main__':
    cli()