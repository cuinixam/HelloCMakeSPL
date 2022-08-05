from pathlib import Path

from HelloCMakeSPL.common.path_with_root import PathWithRoot
from HelloCMakeSPL.project.project import Project
from HelloCMakeSPL.project.project_variant import ProjectVariant


class ProjectArtifacts:
    def __init__(self, project: Project):
        self.project = project
        self.variants_dir = PathWithRoot(self.root_dir, Path('variants'))
        self.src_dir = PathWithRoot(self.root_dir, Path('src'))

    @property
    def root_dir(self) -> Path:
        return self.project.root_dir

    def get_build_dir(self, variant: ProjectVariant, build_kit: str) -> Path:
        return self.root_dir.joinpath(f"build/{variant}/{build_kit}")
