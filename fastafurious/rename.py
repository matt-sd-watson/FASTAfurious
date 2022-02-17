import pandas as pd
import os
import argparse
from Bio import SeqIO

def register_arguments(parser):
    parser.add_argument('--sample_ids', '-s', type=str, help='Sample ID txt file with current and new names',
                        required=True)
    parser.add_argument('--input_fasta', '-i', type=str, help='Input multi-fasta to convert', required=True)
    parser.add_argument('--output_fasta', '-o', type=str, help='Output file with rename headers',
                        required=True)
    parser.add_argument('--original_name', '-1', type=str, help='Column header for the existing FASTA headers',
                        required=True)
    parser.add_argument('--new_name', '-2', type=str, help='Column header for the new FASTA headers',
                        required=True)
    parser.add_argument('--keep-all', "-k", action="store_true",
                        help="If a name match is not found in the renaming CSV, retain sequence with the original name "
                             "instead of removing it.", dest = "keep_all")


def run(args):

    metadata = pd.read_csv(args.sample_ids, sep=",")
    # change the first variable to whatever the name of the column is that contain the names that you will change to
    # the index will have the names that match the current fasta names before renaming
    try:
        data_dict = pd.Series(metadata[str(args.new_name)].values, index=metadata[str(args.original_name)]).to_dict()
       
    except TypeError:
        data_dict = None
        print("The renaming dictionary could not be created:\n {}".format(data_dict))

    fasta_sequences = SeqIO.parse(open(args.input_fasta), 'fasta')

    all_in_fasta = []
    with open(args.output_fasta, "w") as handle:
        for record in fasta_sequences:
            all_in_fasta.append(record.id)
            new_name = str(data_dict.get(record.id))
            if new_name != "None":
                record.id = new_name
                record.description = record.id
                SeqIO.write(record, handle, "fasta")
            else:
                if args.keep_all:
                    record.id = record.id
                    SeqIO.write(record, handle, "fasta")
                    print("WARNING: the following record has no match in samples IDs and will be kept with the original name: {}"
                          .format(record.id))
                else:
                    pass
                    print("WARNING: --keep-all is disabled. The following record has no match in samples IDs and will be removed: {}"
                          .format(record.id))


    missing_from_fasta = [i for i in set(data_dict.keys()) if i not in all_in_fasta]
    if len(missing_from_fasta) > 0:
        print("WARNING: the following records are in the Sample IDs but missing from the input FASTA:")
        print(*missing_from_fasta, sep="\n")