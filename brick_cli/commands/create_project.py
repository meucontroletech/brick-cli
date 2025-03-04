import click

from brick_cli.brick import Brick


@click.command()
@click.argument('project_name', default=None, required=False)
@click.argument('base_dir', default='.', required=False)
def create_project(
    project_name, base_dir
):
    Brick().create_project(project_name, base_dir)
