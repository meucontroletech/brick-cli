import os
from typing import Optional, Literal
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def create_project(
    project_name: Optional[str] = None, base_dir: str = '.'
):
    if project_name:
        os.mkdir(project_name)
        base_dir = os.path.join(base_dir, project_name)

    Path(os.path.join(base_dir, 'src', 'domain', 'entities')).mkdir(
        parents=True, exist_ok=True
    )
    Path(os.path.join(base_dir, 'src', 'domain', 'repositories')).mkdir(
        parents=True, exist_ok=True
    )
    Path(os.path.join(base_dir, 'src', 'application', 'usecases')).mkdir(
        parents=True, exist_ok=True
    )
    Path(os.path.join(base_dir, 'src', 'infra', 'db')).mkdir(
        parents=True, exist_ok=True
    )
    Path(os.path.join(base_dir, 'src', 'infra', 'db', 'models')).mkdir(
        parents=True, exist_ok=True
    )
    Path(os.path.join(base_dir, 'src', 'infra', 'repositories')).mkdir(
        parents=True, exist_ok=True
    )
    Path(os.path.join(base_dir, 'src', 'interface', 'http')).mkdir(
        parents=True, exist_ok=True
    )
    Path(os.path.join(base_dir, 'src', 'interface', 'cli')).mkdir(
        parents=True, exist_ok=True
    )


def create_repository(
    entity_name: str,
    plural_name: Optional[str] = None,
    is_abstract: bool = True,
    db_backend: Literal['sqlalchemy'] = 'sqlalchemy',
    templates_path: Optional[str] = None,
):
    templates_path = templates_path or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'templates'
    )

    env = Environment(loader=FileSystemLoader(templates_path))

    if is_abstract:
        template = env.get_template('abstract_repository.py.jinja2')
    else:
        template = env.get_template(f'{db_backend}_repository.py.jinja2')

    context = {
        'entity': entity_name,
        'plural': plural_name or f'{entity_name}s',
    }

    output = template.render(context)

    if is_abstract:
        path = os.path.join(
            'src',
            'domain',
            'repositories',
            f'{entity_name.lower()}_repository.py',
        )
    else:
        path = os.path.join(
            'src',
            'infra',
            'repositories',
            f'{entity_name.lower()}_repository_{db_backend}.py',
        )

    with open(path, 'w') as f:
        f.write(output)


def create_usecases():
    pass
