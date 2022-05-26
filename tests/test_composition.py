import os
import subprocess
import pytest

def test_composition_default_params(get_merged_seq_path):
    results = subprocess.check_output(
        ['fastafurious', 'composition', '-i', get_merged_seq_path])

    assert all(elem in ["WARNING: The following sequences are too short for analysis: Sequence: Focal_1, Length: 29684",
            "WARNING: The following sequences are too short for analysis: Sequence: Focal_2, Length: 29683",
            "WARNING: The following sequences are too short for analysis: Sequence: Background_1, Length: 29630",
            "WARNING: The following sequences are too short for analysis: Sequence: Background_5, Length: 29629"] for 
               elem in results.decode('utf-8').splitlines())


def test_composition_modify_length(get_merged_seq_path):
    results = subprocess.check_output(
        ['fastafurious', 'composition', '-i', get_merged_seq_path, '-l', '29630'])

    assert "WARNING: The following sequences are too short for analysis: Sequence: Background_5, Length: 29629" in \
           results.decode('utf-8').splitlines()

    assert all(elem not in ["WARNING: The following sequences are too short for analysis: Sequence: Focal_1, "
                            "Length: 29684",
            "WARNING: The following sequences are too short for analysis: Sequence: Focal_2, Length: 29683",
            "WARNING: The following sequences are too short for analysis: Sequence: Background_1, Length: 29630"] for
               elem in results.decode('utf-8').splitlines())

