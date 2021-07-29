import pandas as pd
import os
import argparse

# Author    Matthew Watson  January 18 2021
# This script takes as input a single multi-FASTA with a corresponding
# samples txt file and renames the files to the target name, as well as changes
# the fasta header to match the new file name

# read the metadata file and create a dataframe with the names
# the format of the metadata should be as follows:
# column 1 - WGS_Id- the name of the sample as tracked by Access and Labware
# other column header - gisaid_virus_name_short- the target name for the sample (final NML name)
# other column header - covv_virus_name- the target name for the sample (final Gisaid name)

# NOTE: if the header is going to have / in them, you cannot write the file name to be the same,
# as you cannot have / in filenames

# parse the command line arguments


def register_arguments(parser):
    parser.add_argument('--sample_ids', '-s', type=str, help='Sample ID txt file with current and new names',
                        required=True)
    parser.add_argument('--input_fasta', '-i', type=str, help='Input multi-fasta to convert', required=True)
    parser.add_argument('--output_dir', '-o', type=str, help='output directory for single modified fasta files',
                        required=True)
    parser.add_argument('--category', '-c', type=str, help='Renaming category: NML or Gisaid',
                        required=True)


def run(args):

    # parser = argparse.ArgumentParser(description='Process fasta files and rename for Gisaid')
    # args = parser.parse_args()

    metadata = pd.read_csv(args.sample_ids, sep=",")
    # change the first variable to whatever the name of the column is that contain the names that you will change to
    # the index will have the names that match the current fasta names before renaming

    if args.category == "NML":
        data_dict = pd.Series(metadata.gisaid_virus_name_short.values, index=metadata.WGS_Id).to_dict()
    elif args.category == "Gisaid":
        data_dict = pd.Series(metadata.covv_virus_name.values, index=metadata.WGS_Id).to_dict()

    fasta_to_open = open(args.input_fasta)

    # assert len(fasta_to_open.readlines()) == len(data_dict)

    fasta_name_new = str(os.path.basename(fasta_to_open.name)).strip('.fa') + "_renamed_{}.fa".format(str(args.category))

    output_fasta = os.path.join(args.output_dir, fasta_name_new)

    newfasta = open(output_fasta, 'w')

    content_counts = 0

    for line in fasta_to_open:
        if line.startswith('>'):
            content_counts += 1
        # if the line is a header, make it the same as the file name
        # make sure to strip twice to remove any new line features
            line_cleaned = line.strip('>').strip()
            replacement_line = str(data_dict.get(line_cleaned))
        # ensure that the replacement header is written to a single line
        # write the file contents to the newly named file
            newfasta.write(">" + replacement_line + "\n")
        # if the line is not a header, write identical lines to the new fasta
        else:
            newfasta.write(line)

    fasta_to_open.close()
    newfasta.close()
    assert content_counts == len(data_dict)
