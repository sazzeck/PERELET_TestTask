import typing as t
from math import sqrt


class Matrix:
    def __init__(self, matrix: str) -> None:
        self._numbers: t.List[int] = self._clear_matrix(matrix)
        self._size: int = len(self._numbers)
        self._base_matrix: t.List[t.List[int]] = self._create_matrix()

    def _clear_matrix(self, matrix: str) -> t.List[int]:
        return [int(item) for item in matrix.split() if item.isdigit()]

    def _create_matrix(self) -> t.List[t.List[int]]:
        return [
            self._numbers[item: item + int(sqrt(self._size))]
            for item in range(0, self._size, int(sqrt(self._size)))
        ]

    def spiral_order(self) -> t.List[int]:
        result: t.List[int] = []
        while self._base_matrix:
            result += self._base_matrix.pop(-1)[::-1]
            self._base_matrix = (list(zip(*self._base_matrix)))[::-1]
        return result
