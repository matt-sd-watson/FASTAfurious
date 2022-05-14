from setuptools import setup
from fastafurious import __version__, _program
import os

base_dir = Path(__file__).parent.resolve()
readme_file = os.path.join(base_dir, "README.md")

with readme_file.open(encoding = "utf-8") as f:
    readme_description = f.read()

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
    long_description = readme_description,
    install_requires = ["pandas>=1.1.5", "numpy>=1.19", "biopython>=1.79"],
    entry_points="""
    [console_scripts]
    {program} = fastafurious.__main__:main
    """.format(program=_program),
    include_package_data=True,
)

