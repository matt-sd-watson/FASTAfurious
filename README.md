# FASTAfurious
[![PyPI version](https://badge.fury.io/py/fastafurious.svg)](https://badge.fury.io/py/fastafurious)
![example workflow](https://github.com/matt-sd-watson/FASTAfurious/actions/workflows/main.yml/badge.svg) \
Bundled utilities for manipulation and integration of FASTA files

FASTAfurious provides a set of utilities for the following routine FASTA modifications: 
- creating a FASTA subset based on a list of sequence names (inclusion or exclusion)
- printing statistics and filtering sequences based on genome completeness and length
- renaming fasta headers based on a data sheet

# Installation

```
git clone https://github.com/matt-sd-watson/FASTAfurious.git && cd FASTAfurious
conda env create -f environment.yml
conda activate fastafurious
pip install . 
```

# Updating
```
cd FASTAfurious && git pull
pip install . 
```

# Usage

```
fastafurious -h
usage: fastafurious [-h] {filter,composition,subset,rename,compare} ...

fastafurious: Bundled utilities for manipulating and integrating FASTA files

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  fastafurious provides a series of bundled functions to 
  easily manipulate and integrate FASTA FILES into routine 
  bioinformatics workflows

  {filter,composition,subset,rename,compare}
    filter              filter sequences in FASTA based on completeness and length
    composition         Print the composition statistics of FASTA sequences (completeness/length)
    subset              Create a FASTA subset based on a txt list or bash record input
    rename              Rename the headers of a fasta file based on the columns of a CSV file
    compare             Compare the header entries of two FASTA input files
    version             Print the current FASTAfurious version then exit.
```

# Acknowledgments

code for fastafurious subset was based on the python script originally written by santiagosnchez [here](https://github.com/santiagosnchez/faSomeRecords)
