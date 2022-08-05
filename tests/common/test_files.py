import time

from HelloCMakeSPL.common.text_file import TextFileGenerator
from tests.utils import TestUtils


def test_create_file():
    out_dir = TestUtils.create_clean_test_dir('')
    my_file = out_dir.joinpath('my_file.txt')
    iut = TextFileGenerator(my_file)
    assert not my_file.exists()
    iut.generate_file()
    assert my_file.exists()
    assert my_file.read_text() == ''
    "change content"
    iut.update_content('new')
    iut.generate_file()
    assert my_file.read_text() == 'new'
    "do not write the file if content is the same"
    write_timestamp = my_file.stat().st_ctime_ns
    time.sleep(0.1)
    iut.generate_file()
    new_write_timestamp = my_file.stat().st_ctime_ns
    assert write_timestamp == new_write_timestamp


def test_generated_file():
    out_dir = TestUtils.create_clean_test_dir('')

    my_var = "world!"

    def content_generator():
        return "Hello " + my_var

    my_file = TextFileGenerator(out_dir.joinpath('my_file.txt'), generator=content_generator)
    assert my_file.generate_text() == "Hello world!"
