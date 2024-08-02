import click

@click.group()
def cli():
    pass

@click.command()
def print_message():
    print("printing ....")

cli.add_command(print_message)

if __name__ == '__main__':
    cli()