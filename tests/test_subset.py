import os
import subprocess
import pytest
from Bio import SeqIO


@pytest.fixture
def get_data_dir():
    return str(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/')))


@pytest.fixture
def get_merged_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'merged_seqs.fa'))


@pytest.fixture
def get_subset_list_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'subset_list.txt'))


@pytest.fixture
def get_subset_output_file(tmp_path):
    return str(os.path.join(tmp_path, 'temp.fa'))


@pytest.fixture
def subset_include():
    return ["Focal_2", "Focal_3", "Focal_4", "Background_1", "Background_3", "Background_4"]


@pytest.fixture
def subset_exclude():
    return ["Focal_1", "Background_2", "Background_5", "Background_6"]


def test_subset_simple(get_merged_seq_path, get_subset_output_file, get_subset_list_path,
                       subset_exclude, subset_include):
    results = subprocess.check_output(
        ['fastafurious', 'subset', '-f', get_merged_seq_path,
         '-o', get_subset_output_file, '-l', get_subset_list_path])

    assert len(list(SeqIO.parse(get_subset_output_file, "fasta"))) == 6

    assert "Found 6 sequence(s)" in results.decode('utf-8').splitlines()
    assert "Sequences saved to {}".format(get_subset_output_file) in results.decode('utf-8').splitlines()
    names_in_fasta = []
    for record in SeqIO.parse(get_subset_output_file, "fasta"):
        names_in_fasta.append(record.id)
    assert all(elem in subset_include for
               elem in names_in_fasta)
    assert all(elem not in subset_exclude for
               elem in names_in_fasta)


def test_subset_exclude(get_merged_seq_path, get_subset_output_file, get_subset_list_path,
                        subset_include, subset_exclude):
    subprocess.check_output(
        ['fastafurious', 'subset', '-f', get_merged_seq_path,
         '-o', get_subset_output_file, '-l', get_subset_list_path, '-e'])

    assert len(list(SeqIO.parse(get_subset_output_file, "fasta"))) == 4

    names_in_fasta = []
    for record in SeqIO.parse(get_subset_output_file, "fasta"):
        names_in_fasta.append(record.id)
    assert all(elem in subset_exclude for
               elem in names_in_fasta)
    assert all(elem not in subset_include for
               elem in names_in_fasta)
