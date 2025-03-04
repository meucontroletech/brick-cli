import os

from .abstract_backend import DbBackend


class SQLAlchemyBackend(DbBackend):
    def get_repository_template(self) -> str:
        return 'sqlalchemy_repository.py.jinja2'

    def get_repository_base_path(self) -> str:
        return os.path.join('src', 'infra', 'repositories')

    def get_model_template(self) -> str:
        return 'sqlalchemy_model.py.jinja2'
