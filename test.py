import asyncio
from pprint import pprint

from pygelbooru.gelbooru import Gelbooru


async def main():
    g = Gelbooru()
    return await g.get_posts(tags=['peeing'])

r = asyncio.run(main())
pprint(r)
