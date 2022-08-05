from typing import TypeVar, Generic

T = TypeVar("T")


class Optional(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def get(self) -> T:
        if not self.is_present():
            raise ValueError("Cannot call get on empty optional")
        return self._value

    def get_or_else(self, val: T = None) -> T:
        if not self.is_present():
            return val
        return self._value

    def is_present(self) -> bool:
        return self._value is not None

    def if_present(self, func: callable):
        if self.is_present():
            func(self.get())

    def map(self, transform_callable: callable):
        if self.is_present():
            return type(self)(transform_callable(self.get()))
        else:
            raise ValueError("Cannot map an empty optional")

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Optional) and o._value == self._value

    @classmethod
    def empty(cls):
        return cls[T](None)
