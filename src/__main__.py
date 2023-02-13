import asyncio

from .contrib import parse_matrix


URL: str = "https://raw.githubusercontent.com/koury/pymx/main/source.txt"


if __name__ == "__main__":
    print(asyncio.run(parse_matrix(URL)))
