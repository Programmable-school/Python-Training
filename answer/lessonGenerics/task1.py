"""
課題 Generics
"""

from typing import TypeVar, Sequence

T = TypeVar('T')


def show_generics(a: Sequence[T]):
    print(a)


show_generics([1, 2, 3])
show_generics(['a', 'b', 'c'])
