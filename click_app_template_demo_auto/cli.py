"""Sample click app"""

import click


@click.group()
@click.version_option()
def cli():
    "Demonstrating https://github.com/AH-Merii/click-app"


@cli.command(name="command")
@click.argument("example")
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    if example:
        click.echo(f"You passed example: {example}")
    if option:
        click.echo(f"You passed option: {option}")
    click.echo("Here is some output")
