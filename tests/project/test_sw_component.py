import unittest

from HelloCMakeSPL.project.sw_component import SwComponentBuilder


class TestSwComponent(unittest.TestCase):
    def test_with_name(self):
        builder = SwComponentBuilder()
        sw_comp = builder.with_name("my_comp").with_location("App").create()
        self.assertEqual(sw_comp.name, "my_comp")
        self.assertEqual(sw_comp.location.get(), "App")
