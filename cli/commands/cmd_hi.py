import click


@click.command()
@click.argument("name", default="World")
def cli(name):
    """
    Print a hi message.

    :param name: Name to greet
    :return: None
    """
    click.echo(f"hi {name}")
