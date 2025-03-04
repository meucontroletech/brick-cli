import click

from brick_cli.services import create_project as create_project_service


@click.command()
@click.argument('project_name', default=None, required=False)
@click.argument('base_dir', default='.', required=False)
def create_project(
    project_name, base_dir
):
    create_project_service(project_name, base_dir)
