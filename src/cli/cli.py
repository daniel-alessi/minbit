from functools import lru_cache

import click

from src.core.MinBit import MinBit


@click.group()
def cli():
    pass

@lru_cache(maxsize=1)
def get_minbit() -> MinBit:
    return MinBit()

@click.command()
@click.option('--wallet', '-w', default=None, help='Wallet Alias')
@click.option('--address', '-a', default=None, help='Wallet Address')
@click.option('--key', '-k', default=None, help='Wallet Key')
def mkwallet(wallet: str, address: str, key: str):
    get_minbit().make_wallet(alias=wallet, address=address, key=key)

@click.command()
@click.option('--explicit', '-x', is_flag=True, help='show passwords')
def lwallet(explicit: bool):
    get_minbit().list_wallet(explicit=explicit)

@click.command()
@click.option('--address', '-a', required=True, help='wallet address')
def look(address: str):
    get_minbit().look(address=address)

cli.add_command(mkwallet)
cli.add_command(lwallet)
cli.add_command(look)



if __name__ == '__main__':
    cli()