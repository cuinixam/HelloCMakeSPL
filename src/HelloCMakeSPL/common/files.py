from typing import List

from HelloCMakeSPL.common.text_file import TextFileGenerator


def write_files(files: List[TextFileGenerator]):
    for file in files:
        file.generate_file()
