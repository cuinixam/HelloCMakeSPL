from abc import ABC, abstractmethod


class ProjectGenerator(ABC):
    @abstractmethod
    def generate(self):
        raise NotImplemented
