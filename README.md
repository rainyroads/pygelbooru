# PyGelbooru
![GitHub](https://img.shields.io/github/license/FujiMakoto/pygelbooru)

PyGelbooru is an unofficial and lightweight asynchronous library for the [Gelbooru](https://gelbooru.com/) API.

# Installation
This library requires [Python 3.6](https://www.python.org) or above.

You can install the library through pip as follows,
```shell script
pip install pygelbooru
```

## Usage
The primary use for this library is, naturally, to search for images with specific tags.

This can be done as so:
```python
from pygelbooru import Gelbooru

# API key/user ID is optional, but access may be limited without them
gelbooru = Gelbooru('API_KEY', 'USER_ID')

results = gelbooru.search_posts(tags=['dog ears', '1girl'], exclude_tags=['nude'])
[<GelbooruImage(id=5105386, filename='b77e69be0a4b...dde071dc.jpeg', owner='anon2003')>,
 <GelbooruImage(id=5105161, filename='bf169f891ebe...02bceb5e.jpeg', owner='cpee')>,
 <GelbooruImage(id=5104148, filename='46df3ebe2d41...4316d218e.jpg', owner='danbooru')>,
 <GelbooruImage(id=5104080, filename='e8eec23d151e...419293401.png', owner='anon2003')>,
 <GelbooruImage(id=5103937, filename='5bf279f3c546...be3fc53c8.jpg', owner='danbooru')>,
 ...
 ```
Tags **can** contain spaces when passed as arguments, they will simply be reformated with underscores before being queried, so you don't need to reformat them yourself.

Results are returned as a list of GelbooruImage containers. When cast to a string, this will return the image_url,
```python
str(results[0])
'https://img2.gelbooru.com/images/b7/7e/b77e69be0a4b581eac597527dde071dc.jpeg'
```

You can also pull other information returned by the API,
```python
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
```

### Other methods
In addition to searching for images, you can pull information on tags as follows,
```python
gelbooru.tag_list(name='dog ears')

{'ambiguous': '0',
 'count': '22567',
 'id': '773',
 'tag': 'dog_ears',
 'type': 'tag'}
```

## ToDo
Support for fetching post comments and checking against gelbooru's deleted image hash list.
