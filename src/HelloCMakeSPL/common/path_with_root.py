from pathlib import Path
from typing import Union

from HelloCMakeSPL.common.generic_optional import Optional


class PathWithRoot:

    def __init__(self, root_dir: Path, rel_path: Union[str, Path] = None):
        self.root_dir = root_dir.absolute()
        if rel_path:
            self.rel_path: Optional[Path] = Optional(rel_path) if isinstance(rel_path, Path) \
                else Optional(Path(rel_path))
        else:
            self.rel_path = Optional.empty()

    def to_absolute(self) -> Path:
        if self.rel_path.is_present():
            return self.root_dir.joinpath(self.rel_path.get())
        else:
            return self.root_dir

    def exists(self) -> bool:
        return self.to_absolute().exists()

    def to_relative(self) -> Optional[Path]:
        return self.rel_path

    def to_relative_to_str(self) -> str:
        if self.to_relative().is_present():
            return f"{self.to_relative().get()}"
        return ''

    def joinpath(self, rel_path: str):
        if not self.rel_path.is_present():
            self.rel_path = Optional(Path(rel_path))
        else:
            self.rel_path = self.rel_path.map(lambda x: x.joinpath(rel_path))
        return self
