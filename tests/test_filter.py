import os
import subprocess
import pytest
from Bio import SeqIO


@pytest.fixture(scope = "module")
def get_data_dir():
    return str(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/')))


@pytest.fixture(scope = "module")
def get_merged_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'merged_seqs.fa'))


@pytest.fixture(scope = "function")
def get_filtered_output_file(tmp_path):
    return str(os.path.join(tmp_path, 'temp.fa'))


def test_filter_high_length(get_merged_seq_path, get_filtered_output_file):
    results = subprocess.check_output(
        ['fastafurious', 'filter', '-i', get_merged_seq_path,
         '-l', '29800', '-o', get_filtered_output_file])

    assert len(list(SeqIO.parse(get_filtered_output_file, "fasta"))) == 2

    assert "2 sequences written to {}".format(get_filtered_output_file) in results.decode('utf-8').splitlines()
