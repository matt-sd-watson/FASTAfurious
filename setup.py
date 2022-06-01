from setuptools import setup
from fastafurious import __version__, _program
import os
from pathlib import Path

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='fastafurious',
    version=__version__,
    packages=['fastafurious'],
    package_dir={'fastafurious': 'fastafurious'},
    url='https://github.com/matt-sd-watson/FASTAfurious/',
    project_urls = {
        "Issues": "https://github.com/matt-sd-watson/FASTAfurious/issues",
        "Source": "https://github.com/matt-sd-watson/FASTAfurious",
    },
    license='',
    author='Matthew Watson',
    author_email='matthew.watson@uhn.ca',
    description='Bundled utilities for manipulating and integrating FASTA files',
    long_description = long_description,
    install_requires = ["pandas>=1.1.5", "numpy>=1.19", "biopython>=1.79", "pypandoc>=1.8",
                        "pytest>=7.1.2"],
    entry_points="""
    [console_scripts]
    {program} = fastafurious.__main__:main
    """.format(program=_program),
    include_package_data=True,
)

