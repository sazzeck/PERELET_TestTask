import typing as t

import aiohttp

from .matrix import Matrix


async def _fetch_matrix(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.ok:
                return await response.text()


async def parse_matrix(url: str) -> t.List[int]:
    matrix: Matrix = Matrix(await _fetch_matrix(url))
    return matrix.spiral_order()
