import os
import subprocess
import pytest

@pytest.fixture(scope = "module")
def get_data_dir():
    return str(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/')))


@pytest.fixture(scope = "module")
def get_first_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'focal_seqs.fa'))


@pytest.fixture(scope = "module")
def get_second_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'background_seqs.fa'))


@pytest.fixture(scope = "module")
def get_merged_seq_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'merged_seqs.fa'))

@pytest.fixture(scope = "function")
def get_temp_output_file(tmp_path):
    return str(os.path.join(tmp_path, 'temp.fa'))

@pytest.fixture(scope = "module")
def get_partial_renaming_csv(get_data_dir):
    return str(os.path.join(get_data_dir, 'names_partial.csv'))


@pytest.fixture(scope = "module")
def get_full_renaming_csv(get_data_dir):
    return str(os.path.join(get_data_dir, 'names_complete.csv'))

@pytest.fixture(scope = "module")
def get_input_header_name():
    return ["-1", "original_name", "-2", "new_name"]

@pytest.fixture(scope = "module")
def get_subset_list_path(get_data_dir):
    return str(os.path.join(get_data_dir, 'subset_list.txt'))

@pytest.fixture(scope = "module")
def subset_include():
    return ["Focal_2", "Focal_3", "Focal_4", "Background_1", "Background_3", "Background_4"]

@pytest.fixture(scope = "module")
def subset_exclude():
    return ["Focal_1", "Background_2", "Background_5", "Background_6"]