import click

from brick_cli.services import create_repository as create_repository_service


@click.command()
@click.argument('entity_name')
@click.option('--plural_name', default=None, required=False)
@click.option('--is_abstract', default=True, required=False)
@click.option(
    '--repository_backend',
    default='sqlalchemy',
    type=click.Choice(['sqlalchemy']),
    required=False,
)
@click.option('--templates-path', default=None, required=False)
def create_repository(
    entity_name, plural_name, is_abstract, repository_backend, templates_path
):
    create_repository_service(
        entity_name,
        plural_name,
        is_abstract,
        repository_backend,
        templates_path,
    )
