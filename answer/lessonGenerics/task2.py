"""
課題 Generics
"""

from typing import TypeVar, Generic

T = TypeVar('T')


class Model(Generic[T]):
    value: T

    def __init__(self):
        pass

    def set_value(self, value: T):
        self.value: T = value

    def get_value(self) -> T:
        return self.value


model1 = Model[int]()
model1.set_value(123)
print(model1.get_value())

model2 = Model[str]()
model2.set_value('aiueo')
print(model2.get_value())
