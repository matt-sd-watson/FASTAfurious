import os
import subprocess
import pytest


@pytest.fixture
def get_data_dir():
    return str(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/')))


@pytest.fixture
def get_first_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'focal_seqs.fa'))


@pytest.fixture
def get_second_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'background_seqs.fa'))


@pytest.fixture
def get_merged_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'merged_seqs.fa'))


def test_compare_two_different_fastas(get_first_seq_path, get_second_seq_path):
        results = subprocess.run(
            ['fastafurious', 'compare', '-1', get_first_seq_path,
             '-2', get_second_seq_path], stdout=subprocess.PIPE)

        assert "No matching FASTA sequences were found between both input files" in results.stdout.decode('utf-8')


def test_compare_overlapping_fastas(get_first_seq_path, get_merged_seq_path):
    results = subprocess.run(
        ['fastafurious', 'compare', '-1', get_first_seq_path,
         '-2', get_merged_seq_path], stdout=subprocess.PIPE)

    assert "Number of matching FASTA sequences: 4" in results.stdout.decode('utf-8')
    assert "Background_" not in results.stdout.decode('utf-8')
    assert "Focal_" in results.stdout.decode('utf-8')
