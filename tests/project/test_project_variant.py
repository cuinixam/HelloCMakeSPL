import pytest

from HelloCMakeSPL.project.project_variant import ProjectVariant


class TestProjectVariant:
    @pytest.mark.parametrize(
        "variant,flavor,subsystem",
        [
            ("MY/VAR", "MY", "VAR"),
            ("MY\\VAR", "MY", "VAR")
        ],
    )
    def test_from_str(self, variant, flavor, subsystem):
        iut = ProjectVariant.from_str(variant)
        assert iut.flavor == flavor
        assert iut.subsystem == subsystem
        assert f"{iut}" == "MY/VAR"

    def test_incorrect_variant(self):
        with pytest.raises(ValueError):
            ProjectVariant.from_str('MY_VAR')
