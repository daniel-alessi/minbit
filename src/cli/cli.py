import click

@click.group()
def cli():
    pass

@click.command()
def hello():
    """Simple program that says hello."""
    click.echo('Hello, User!')

@click.command()
@click.argument('name')
def greet(name):
    """Greet the user by name."""
    click.echo(f'Hello, {name}!')

@click.command()
@click.argument('number1', type=int)
@click.argument('number2', type=int)
def add(number1, number2):
    """Add two numbers."""
    result = number1 + number2
    click.echo(f'The result is {result}')

# Add commands to the CLI group
cli.add_command(hello)
cli.add_command(greet)
cli.add_command(add)

if __name__ == '__main__':
    cli()