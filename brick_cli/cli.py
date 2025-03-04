import click

from brick_cli.commands import (
    create_repository,
    create_project,
    create_usecases,
)


@click.group()
def cli():
    pass


cli.add_command(create_repository)
cli.add_command(create_project)
cli.add_command(create_usecases)
# TODO: brick generate module user


if __name__ == '__main__':
    cli()
