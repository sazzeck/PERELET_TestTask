import asyncio
import typing as t
import unittest

from src import parse_matrix


class ParseMatrixTest(unittest.TestCase):
    URL: str = "https://raw.githubusercontent.com/koury/pymx/main/source.txt"

    EXPECTED: t.List[str] = [
        160,
        150,
        140,
        130,
        90,
        50,
        10,
        20,
        30,
        40,
        80,
        120,
        110,
        100,
        60,
        70,
    ]

    def test_parse_matrix(self) -> None:
        spiral_matrix: t.List[int] = asyncio.run(parse_matrix(self.URL))
        self.assertEqual(spiral_matrix, self.EXPECTED)


if __name__ == "__main__":
    unittest.main()
