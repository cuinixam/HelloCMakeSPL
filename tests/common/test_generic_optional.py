from unittest.mock import MagicMock

import pytest

from HelloCMakeSPL.common.generic_optional import Optional


def test_get():
    my_var = Optional(2)
    assert my_var.is_present()
    assert my_var.get() == 2


def test_empty():
    assert not Optional.empty().is_present()
    assert Optional.empty() == Optional(None)


def test_incorrect_variant():
    with pytest.raises(ValueError) as e:
        Optional.empty().get()
    assert str(e.value) == "Cannot call get on empty optional"


def test_if_present():
    my_mock = MagicMock()

    Optional.empty().if_present(my_mock.func)
    my_mock.func.assert_not_called()

    Optional("Hello world!").if_present(my_mock.func)
    my_mock.func.assert_called_once_with("Hello world!")


def test_map():
    my_var = Optional("Hello")
    new_var = my_var.map(lambda x: x.upper())
    assert new_var.is_present()
    assert new_var.get() == "HELLO"
    assert my_var.get() == "Hello"
