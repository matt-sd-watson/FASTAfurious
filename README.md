# FASTAfurious
Bundled utilities for manipulation and integration of FASTA files

# Installation

```
git clone https://github.com/matt-sd-watson/FASTAfurious.git && cd FASTAfurious
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
usage: fastafurious [-h] {gisaid,nextstrain,composition,filter,subset} ...

fastafurious: Bundled utilities for manipulating and integrating FASTA files

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  fastafurious provides a series of bundled functions to 
  easily manipulate and integrate FASTA FILES into routine 
  bioinformatics workflows

  {gisaid,nextstrain,composition,filter,subset}
    gisaid              Rename FASTA headers to be compatible with Gisaid submissions
    nextstrain          Rename FASTA hedaers to be compatible with Nextstrain builds
    composition         Print the composition statistics of FASTA sequences
    filter              filter sequences in FASTA based on completeness and length
    subset              Create a FASTA subset based on a txt list of bash record list
```


