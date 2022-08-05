import os
import unittest

from HelloCMakeSPL.cmake.clang_toolchain import ClangToolchain
from HelloCMakeSPL.cmake.cmake import CMake
from HelloCMakeSPL.common.files import write_files
from HelloCMakeSPL.generator.cmake_project_generator import CMakeProjectGenerator
from HelloCMakeSPL.project.project import ProjectBuilder
from HelloCMakeSPL.project.project_artifacts import ProjectArtifacts
from HelloCMakeSPL.project.project_variant import ProjectVariant
from HelloCMakeSPL.project.sw_component import SwComponentBuilder
from tests.utils import TestUtils


class TestSplCMakeProject(unittest.TestCase):
    def test_simple_project(self):
        out_dir = TestUtils.create_clean_test_dir('my_simple_project')
        builder = ProjectBuilder()
        builder.with_name('MySimpleProject').with_out_dir(out_dir.path).with_variant("FLV1/SYS1")
        component = SwComponentBuilder().with_name('Main').with_location('App').with_main_file().create()
        builder.with_component(component)
        project = builder.create()
        files = CMakeProjectGenerator(project, ClangToolchain()).generate()
        self.assertEqual(len(files), 2)
        self.assertTrue(files[0].generate_text().find("cmake_minimum_required"))
        self.assertEqual(project.root_dir, out_dir.joinpath('MySimpleProject'))
        "Write all files to disk"
        write_files(files)
        exec_status = CMake(ProjectArtifacts(project)).run(ProjectVariant.from_str("FLV1/SYS1"), "prod")
        self.assertEqual(exec_status.returncode, 0)
        binary_name = "main.exe" if os.name == 'nt' else "main"
        self.assertTrue(out_dir.joinpath(f"MySimpleProject/build/FLV1/SYS1/prod/{binary_name}").exists())
