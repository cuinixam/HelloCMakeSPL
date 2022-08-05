import dataclasses
from typing import List

from HelloCMakeSPL.common.generic_optional import Optional
from HelloCMakeSPL.common.text_generator import TextGenerator
from HelloCMakeSPL.generator import templates


@dataclasses.dataclass
class ComponentFile:
    name: str
    generator: TextGenerator


@dataclasses.dataclass
class SwComponent:
    name: str
    "defines the component relative path inside the 'src' folder (without the component name)"
    location: Optional[str]
    files: List[ComponentFile]

    @property
    def relpath(self) -> str:
        if self.location.is_present():
            return f"{self.location.get()}/{self.name}"
        else:
            return self.name


class SwComponentBuilder:

    def __init__(self):
        self.name: str = None
        self.location: Optional[str] = Optional.empty()
        self.files: List[ComponentFile] = []

    def with_name(self, name: str):
        self.name = name
        return self

    def with_location(self, location: str):
        self.location = Optional(location)
        return self

    def with_main_file(self):
        return self.with_file('main.c', templates.hello_world_main_c)

    def with_file(self, file_name: str, content: str):
        self.files = self.files or []
        self.files.append(ComponentFile(file_name, TextGenerator(content=content)))
        return self

    def create(self) -> SwComponent:
        return SwComponent(self.name, self.location, self.files)
