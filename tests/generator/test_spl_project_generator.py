import unittest

from HelloCMakeSPL.generator.spl_project_generator import SplProjectGenerator
from tests.utils import TestUtils


class TestSplCMakeProject(unittest.TestCase):
    def ignored_test_materialize_project(self):
        out_dir = TestUtils.create_clean_test_dir('my_simple_spl_project')
        project_description = """
        // This is just a simple definition of a project
        project MyProject
        variant {
            flavor Flv1
            subsystem Sys1 
            components Main Comp1
        }
        variant {
            flavor Flv2
            subsystem Sys2 
            components Main Comp2
        }
        """
        generator = SplProjectGenerator(project_description)
        generator.materialize(out_dir)
        self.assertTrue(out_dir.joinpath('CMakeLists.txt').exists())

    def test_create_project_with_one_variant(self):
        project_description = """
        // This is just a simple definition of a project
        project MyProject
        variant {
            flavor Flv1
            subsystem Sys1 
            components Main Comp1
        }
        variant {
            flavor Flv2
            subsystem Sys2 
            components Main Comp2
        }
        """
        generator = SplProjectGenerator(project_description)
        project = generator.generate()
        self.assertEquals(project.name, "MyProject")
        self.assertEquals(len(project.variants), 2)
