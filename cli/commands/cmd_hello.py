import click


@click.command()
@click.option("--name", default="World", help="Name to greet")
def cli(name):
    """
    Print a hello message.

    :param name: Name to greet
    :return: None
    """
    click.echo(f"Hello, {name}!")
