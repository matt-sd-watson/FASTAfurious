import os
import subprocess
import pytest
from Bio import SeqIO


def test_filter_high_length(get_merged_seq_path, get_temp_output_file):
    results = subprocess.check_output(
        ['fastafurious', 'filter', '-i', get_merged_seq_path,
         '-l', '29800', '-o', get_temp_output_file])

    assert len(list(SeqIO.parse(get_temp_output_file, "fasta"))) == 2

    assert "2 sequences written to {}".format(get_temp_output_file) in results.decode('utf-8').splitlines()
