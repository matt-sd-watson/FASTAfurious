from setuptools import setup
from fastafurious import __version__, _program

setup(
    name='fastafurious',
    version=__version__,
    packages=['fastafurious'],
    package_dir={'fastafurious': 'fastafurious'},
    url='',
    license='',
    author='Matthew Watson',
    author_email='matthew.watson@oahpp.ca',
    description='Bundled utilities for manipulating and integrating FASTA files',
    install_requires = ["pandas>=1.1.5", "numpy>=1.19", "biopython>=1.79"],
    entry_points="""
    [console_scripts]
    {program} = fastafurious.__main__:main
    """.format(program=_program),
    include_package_data=True,
)

