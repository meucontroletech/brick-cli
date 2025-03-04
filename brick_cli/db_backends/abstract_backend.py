from abc import ABC, abstractmethod


class DbBackend(ABC):
    @abstractmethod
    def get_repository_template(self) -> str:
        pass

    @abstractmethod
    def get_repository_base_path(self) -> str:
        pass

    @abstractmethod
    def get_model_template(self) -> str:
        pass
