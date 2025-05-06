import click


@click.group(short_help="ckanstrageapi CLI.")
def ckanstrageapi():
    """ckanstrageapi CLI.
    """
    pass


@ckanstrageapi.command()
@click.argument("name", default="ckanstrageapi")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [ckanstrageapi]
