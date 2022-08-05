from abc import ABC, abstractmethod


class FileGenerator(ABC):
    @abstractmethod
    def generate_text(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate_file(self, only_if_modified: bool = True):
        raise NotImplementedError
