from setuptools import setup
from setuptools import find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude=["tests*"]),
    license= 'MIT',
    description= 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires=['numpy'],
    author='boitumelo',
    author_email='boitumelo@explore.ai'
)