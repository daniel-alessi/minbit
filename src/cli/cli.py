import click

from src.core.MinBit import MinBit


@click.group()
def cli():
    pass

@click.command()
@click.option('--wallet', '-w', default=None, help='Wallet Alias')
@click.option('--address', '-a', default=None, help='Wallet Address')
@click.option('--key', '-k', default=None, help='Wallet Key')
def mkwallet(wallet: str, address: str, key: str):
    MinBit().make_wallet(alias=wallet, address=address, key=key)

@click.command()
@click.option('--explicit', '-x', is_flag=True, help='show passwords')
def lwallet(explicit):
    MinBit().list_wallet(explicit=explicit)

cli.add_command(mkwallet)
cli.add_command(lwallet)


if __name__ == '__main__':
    cli()