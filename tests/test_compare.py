import os
import subprocess
import pytest

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
