from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='pygelbooru',  # How you named your package folder (MyLib)
        packages=['pygelbooru'],  # Chose the same as "name"
        version='0.5.0',  # Start with a small number and increase it with every change you make
        license='gpl-3.0',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
        description='PyGelbooru is an unofficial and lightweight asynchronous library for Gelbooru compatible API\'s.',  # Give a short description about your library
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Makoto',  # Type in your name
        author_email='FujiMakoto@users.noreply.github.com',  # Type in your E-Mail
        url='https://github.com/FujiMakoto/pygelbooru',  # Provide either the link to your github or to your website
        download_url='https://github.com/FujiMakoto/pygelbooru/archive/v0.5.0.tar.gz',
        keywords=['gelbooru', 'anime', 'artwork', 'anime artwork', 'booru'],  # Keywords that define your package best
        install_requires=[
            'aiohttp',
            'furl',
            'xmltodict'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Multimedia :: Graphics',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  # Again, pick a license
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8'
        ],
)
