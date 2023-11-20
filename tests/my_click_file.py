import click


@click.command()
def hello():
    click.echo('Hello, World!')


@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def greet(name, count):
    for _ in range(count):
        click.echo(f'Hello, {name}!')


if __name__ == '__main__':
    hello()
