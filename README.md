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

### Searching
The primary use for this library is, naturally, to search for images with specific tags.

This can be done as so:
```python
from pygelbooru import Gelbooru

# API key/user ID is optional, but access may be limited without them
gelbooru = Gelbooru('API_KEY', 'USER_ID')

results = await gelbooru.search_posts(tags=['dog ears', '1girl'], exclude_tags=['nude'])
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
https://github.com/FujiMakoto/pygelbooru/blob/master/pygelbooru/gelbooru.py#L32-L47

### Searching (Random)
In addition to searching for a large list of images, PyGelbooru also provides a helper method for when you're really just after a single, random image that matches the specified tags.

This method will automatically pull a random image from the last 20,000 Gelbooru image submissions.

```python
result = await gelbooru.random_post(tags=['cat ears', '1girl', 'cat hood', 'bell'], exclude_tags=['nude'])
<GelbooruImage(id=5106718, filename='bbbdfbf9e883...161753514.png', owner='6498')>
```

### Comments

You can fetch post comments directly from the GelbooruImage container,
```python
post = await gelbooru.get_post(5099841)
await post.get_comments()
[<GelbooruComment(id=2486074, author='Anonymous', created_at='2020-01-28 08:47')>]
```

### Tags
Besides searching for images, you can also pull information on tags as follows,
```python
await gelbooru.tag_list(name='dog ears')
<GelbooruTag(id=773, name='dog_ears', count=22578)>

# Use "name_pattern" to search for partial matches to a specified tag
await gelbooru.tag_list(name_pattern='%splatoon%', limit=4)
[<GelbooruTag(id=892683, name='splatoon_(series)', count=11353)>,
 <GelbooruTag(id=759189, name='splatoon_2', count=3488)>,
 <GelbooruTag(id=612372, name='aori_(splatoon)', count=2266)>,
 <GelbooruTag(id=612374, name='hotaru_(splatoon)', count=2248)>]
```
