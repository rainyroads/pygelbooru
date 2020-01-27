import reprlib
from typing import *

import aiohttp
from furl import furl


class GelbooruException(Exception):
    pass


class GelbooruNotFoundException(GelbooruException):
    pass


class GelbooruImage:
    """
    Container for Gelbooru image results.

    Returns the image URL when cast to str
    """
    def __init__(self, payload: dict):
        self.id         = payload.get('id')
        self.owner      = payload.get('owner')
        self.created_at = payload.get('created_at')
        self.file_url   = payload.get('file_url')
        self.filename   = payload.get('image')
        self.source     = payload.get('source') or None
        self.hash       = payload.get('hash')
        self.height     = payload.get('height')
        self.width      = payload.get('width')
        self.rating     = payload.get('q')
        self.has_sample = payload.get('sample')
        self.tags       = str(payload.get('tags')).split(' ')
        self.change     = payload.get('change')
        self.directory  = payload.get('directory')

    def __str__(self):
        return self.file_url

    def __repr__(self):
        rep = reprlib.Repr()
        return f"<GelbooruImage(id={self.id}, filename={rep.repr(self.filename)}, owner={rep.repr(self.owner)})>"


class Gelbooru:
    BASE_URL = 'https://gelbooru.com/'

    def __init__(self, api_key: Optional[str] = None):
        self._api_key = api_key

    async def get_post(self, post_id: int) -> Optional[GelbooruImage]:
        """
        Get a specific Gelbooru post by its ID

        Args:
            post_id (int): The post id to lookup

        Raises:
            GelbooruNotFoundException: Raised if Gelbooru returns an empty result for this query
        """
        endpoint = furl(self.BASE_URL)
        endpoint.args['page'] = 'dapi'
        endpoint.args['s'] = 'post'
        endpoint.args['q'] = 'index'
        endpoint.args['json'] = '1'
        endpoint.args['id'] = post_id

        payload = await self._request(str(endpoint))
        try:
            return GelbooruImage(payload[0])
        except TypeError:
            raise GelbooruNotFoundException(f"Could not find a post with the ID {post_id}")

    async def search_posts(self, *, tags: Optional[List[str]] = None, exclude_tags: Optional[List[str]] = None, limit: int = 100) -> List[GelbooruImage]:
        """
        Search for images with the optionally specified tag(s)

        Args:
            tags (list of str): A list of tags to search for
            exclude_tags (list of str): A list of tags to EXCLUDE from search results
            limit (int): Limit the number of results returned. Maximum value allowed is 100.

        Returns:
            list of GelbooruImage
        """
        endpoint = furl(self.BASE_URL)
        endpoint.args['page']   = 'dapi'
        endpoint.args['s']      = 'post'
        endpoint.args['q']      = 'index'
        endpoint.args['json']   = '1'
        endpoint.args['limit']  = min(limit, 100)

        # Apply basic tag formatting
        tags = [tag.strip().lower().replace(' ', '_') for tag in tags] if tags else []
        exclude_tags = ['-' + tag.strip().lstrip('-').lower().replace(' ', '_') for tag in exclude_tags] if exclude_tags else []

        if tags or exclude_tags:
            endpoint.args['tags'] = ' '.join(tags + exclude_tags)

        payload = await self._request(str(endpoint))
        return [GelbooruImage(p) for p in payload]

    async def _request(self, url: str) -> dict:
        async with aiohttp.ClientSession() as session:
            status_code, response = await self._fetch(session, url)

        if status_code not in [200, 201]:
            raise GelbooruException(f"""Gelbooru returned a non 200 status code: {response}""")

        return response

    async def _fetch(self, session: aiohttp.ClientSession, url) -> Tuple[int, dict]:
        async with session.get(url) as response:
            return response.status, await response.json()
