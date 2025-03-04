import os
from typing import Optional, Literal
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class Brick:
    def __init__(
        self,
        template_path: str = 'brick_cli/templates',
        db_backend: Literal['sqlalchemy'] = 'sqlalchemy',
    ):
        self.template_path = template_path
        self.db_backend = db_backend

    def create_project(
        self, project_name: Optional[str] = None, base_dir: str = '.'
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
        self,
        entity_name: str,
        plural_name: Optional[str] = None,
        is_abstract: bool = True,
    ):
        # Configura o ambiente de Jinja2
        env = Environment(loader=FileSystemLoader(self.template_path))

        # Carrega o template
        if is_abstract:
            template = env.get_template('abstract_repository.py.jinja2')
        else:
            template = env.get_template(
                f'{self.db_backend}_repository.py.jinja2'
            )

        # Define as variáveis que serão passadas para o template
        context = {
            'entity': entity_name,
            'plural': plural_name or f'{entity_name}s',
        }

        # Renderiza o template com o contexto
        output = template.render(context)

        # Exibe o resultado renderizado
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
                f'{entity_name.lower()}_repository_{self.db_backend}.py',
            )

        with open(path, 'w') as f:
            f.write(output)

    def create_usecases(self):
        pass
