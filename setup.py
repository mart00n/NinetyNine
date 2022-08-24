import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
    long_description = file.read()

setup(
    name = "ninetynine",
    version = "0.0.1",
    author = "Andrew Marton",
    author_email = "",
    description = ("The Game of 99 implemented as web app"),
    license = "MIT",
    keywords = "",
    url = "",
    packages = ['ninetynine', 'tests'],
    long_description = long_description,
)