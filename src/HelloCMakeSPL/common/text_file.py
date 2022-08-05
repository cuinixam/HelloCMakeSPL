from pathlib import Path
from typing import Callable

from HelloCMakeSPL.common.generated_file import FileGenerator
from HelloCMakeSPL.common.text_generator import TextGenerator


# Multiple inheritance, maybe you want to read: http://python-history.blogspot.com/2010/06/method-resolution-order.html
class TextFileGenerator(TextGenerator, FileGenerator):

    def __init__(self, filepath: Path, *, generator: Callable[[], str] = None, content: str = None,
                 encoding: str = "utf-8"):
        super().__init__(generator=generator, content=content)
        self.filepath = filepath
        self.encoding = encoding

    def generate_file(self, only_if_modified: bool = True):
        out_dir = self.filepath.parent
        if not out_dir.is_dir():
            out_dir.mkdir(parents=True)
        new_content = self.generate_text().encode(self.encoding)
        if only_if_modified and self.filepath.is_file():
            old_content = self.filepath.read_bytes()
            if new_content == old_content:
                return
        self.filepath.write_bytes(new_content)
