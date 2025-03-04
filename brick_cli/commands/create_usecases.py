import click

from brick_cli.services import create_usecases as create_usecases_service


@click.command()
@click.argument('entity_name')
@click.option('--plural_name', default=None, required=False)
@click.option('--templates-path', default=None, required=False)
def create_usecases(entity_name, plural_name, templates_path):
    create_usecases_service(
        entity_name,
        plural_name,
        templates_path,
    )
