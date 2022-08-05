import dataclasses
from pathlib import Path
from typing import List

from HelloCMakeSPL.project.project_variant import ProjectVariant
from HelloCMakeSPL.project.sw_component import SwComponent


@dataclasses.dataclass(init=False)
class Project:
    root_dir: Path
    name: str
    variants: List[ProjectVariant]
    components: List[SwComponent]


class ProjectBuilder:

    def __init__(self):
        self.out_dir = Path(".")
        self.name = 'NoName'
        self.variants: List[ProjectVariant] = []
        self.components: List[SwComponent] = []

    def with_name(self, name: str):
        self.name = name
        return self

    def with_out_dir(self, out_dir: Path):
        self.out_dir = out_dir
        return self

    def with_variant(self, variant: str):
        self.variants = self.variants or []
        self.variants.append(ProjectVariant.from_str(variant))
        return self

    def with_variants(self, variants: List[str]):
        self.variants = self.variants or []
        self.variants.extend([ProjectVariant.from_str(var) for var in variants])
        return self

    def with_component(self, component: SwComponent):
        self.components = self.components or []
        self.components.append(component)
        return self

    def with_components(self, components: List[SwComponent]):
        self.components = self.components or []
        self.components.extend(components)
        return self

    def create(self) -> Project:
        project = Project()
        project.name = self.name
        project.root_dir = self.out_dir.joinpath(self.name)
        project.variants = self.variants
        project.components = self.components
        return project
