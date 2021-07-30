import pandas as pd
import os
import argparse


def register_arguments(parser):
    parser.add_argument('--sample_ids', '-s', type=str, help='Sample ID txt file with current and new names',
                        required=True)
    parser.add_argument('--input_fasta', '-i', type=str, help='Input multi-fasta to convert', required=True)
    parser.add_argument('--output_dir', '-o', type=str, help='output directory for single modified fasta files',
                        required=True)
    parser.add_argument('--original_name', '-1', type=str, help='Column header for the existing FASTA headers',
                        required=True)
    parser.add_argument('--new_name', '-2', type=str, help='Column header for the new FASTA headers',
                        required=True)


def run(args):

    metadata = pd.read_csv(args.sample_ids, sep=",")
    # change the first variable to whatever the name of the column is that contain the names that you will change to
    # the index will have the names that match the current fasta names before renaming
    try:
        data_dict = pd.Series(metadata[str(args.new_name)].values, index=metadata[str(args.original_name)]).to_dict()
       
    except TypeError:
        data_dict = None
        print("The renaming dictionary could not be created:\n {}".format(data_dict))

    fasta_to_open = open(args.input_fasta)

    fasta_name_new = str(os.path.basename(str(fasta_to_open.name))).split('.fa')[0] + "_renamed.fa"

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
