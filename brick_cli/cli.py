import click

from brick_cli.commands import create_repository, create_project


@click.group()
def cli():
    pass


cli.add_command(create_repository)
cli.add_command(create_project)


if __name__ == '__main__':
    cli()
