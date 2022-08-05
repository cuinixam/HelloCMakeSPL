from pathlib import Path

from HelloCMakeSPL.common.generic_optional import Optional
from HelloCMakeSPL.common.path_with_root import PathWithRoot


def test_path_with_root():
    my_path = PathWithRoot(Path("."), Path("my/path"))
    assert my_path.to_absolute() == Path("./my/path").absolute()
    assert my_path.to_relative() == Optional(Path("my/path"))

    my_path = PathWithRoot(Path("."))
    assert my_path.to_absolute() == Path(".").absolute()

    my_path.joinpath('some/path').joinpath('file.c')
    assert my_path.to_absolute() == Path("./some/path/file.c").absolute()
