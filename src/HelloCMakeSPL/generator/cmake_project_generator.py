import textwrap
from typing import List

from HelloCMakeSPL.cmake.cmake_toolchain import CMakeToolchain
from HelloCMakeSPL.common.generated_file import FileGenerator
from HelloCMakeSPL.common.text_file import TextFileGenerator
from HelloCMakeSPL.generator.project_generator import ProjectGenerator
from HelloCMakeSPL.project.project import Project
from HelloCMakeSPL.project.project_artifacts import ProjectArtifacts


class CMakeProjectGenerator(ProjectGenerator):
    def __init__(self, project: Project, cmake_toolchain: CMakeToolchain):
        self.project = project
        self.artifacts = ProjectArtifacts(project)
        self.cmake_toolchain = cmake_toolchain

    def generate(self) -> List[TextFileGenerator]:
        # TODO: check that the folder is not empty instead of only checking for existence
        if self.project.root_dir.is_dir():
            raise ValueError("Project root exists and might not be empty!")
        generated_files = [self.create_project_cmake_lists()]
        generated_files.extend(self.create_component_files())
        return generated_files

    def create_project_cmake_lists(self) -> TextFileGenerator:
        # TODO: create class for CMakeLists file
        def create_cmake_lists():
            return textwrap.dedent(f"""
                # cmake project definition
                cmake_minimum_required(VERSION 3.18.0)
                
                project({self.project.name})
                
                add_executable(main "src/App/Main/main.c")

            """)

        cmake_lists_file = TextFileGenerator(self.artifacts.root_dir.joinpath('CMakeLists.txt'),
                                             generator=create_cmake_lists)
        return cmake_lists_file

    def create_component_files(self) -> List[FileGenerator]:
        generated_files = []
        for component in self.project.components:
            comp_path = self.artifacts.src_dir.joinpath(component.relpath)
            generated_files.extend([
                TextFileGenerator(comp_path.joinpath(file.name).to_absolute(), generator=file.generator.generator)
                for file in component.files
            ])
        return generated_files
