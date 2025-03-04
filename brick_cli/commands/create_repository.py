import click

from brick_cli.brick import Brick


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
def create_repository(
    entity_name, plural_name, is_abstract, repository_backend
):
    Brick(db_backend=repository_backend).create_repository(
        entity_name, plural_name, is_abstract
    )
