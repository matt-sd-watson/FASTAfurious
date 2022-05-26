import os
import subprocess
import pytest
from Bio import SeqIO


def test_renaming_partial(get_merged_seq_path, get_temp_output_file, get_partial_renaming_csv,
                          get_input_header_name):
    results = subprocess.check_output(
        ['fastafurious', 'rename', '-i', get_merged_seq_path,
         '-o', get_temp_output_file, '-s', get_partial_renaming_csv] + get_input_header_name)

    assert len(list(SeqIO.parse(get_temp_output_file, "fasta"))) == 8

    assert all(elem in ["WARNING: --keep-all is disabled. The following record has no "
                        "match in samples IDs and will be removed: Focal_4",
                        "WARNING: --keep-all is disabled. The following record has no match "
                        "in samples IDs and will be removed: Background_3",
                        "WARNING: the following records are in the Sample IDs "
                        "but missing from the input FASTA:",
                        "Random_1", "Random_2"] for
               elem in results.decode('utf-8').splitlines())


def test_renaming_full(get_merged_seq_path, get_temp_output_file, get_full_renaming_csv,
                       get_input_header_name):
    results = subprocess.check_output(
        ['fastafurious', 'rename', '-i', get_merged_seq_path,
         '-o', get_temp_output_file, '-s', get_full_renaming_csv] + get_input_header_name)

    assert len(list(SeqIO.parse(get_temp_output_file, "fasta"))) == 10
    assert len(results.decode('utf-8').splitlines()) == 0
    names_in_fasta = []
    for record in SeqIO.parse(get_temp_output_file, "fasta"):
        names_in_fasta.append(record.id)
    names_not_all = ['Renamed_1', 'Renamed_2', 'Renamed_3',
                     'Renamed_4', 'Renamed_5', 'Renamed_6', 'Renamed_7',
                     'Renamed_8', 'Renamed_9', 'Renamed_10']
    assert names_in_fasta == names_not_all
