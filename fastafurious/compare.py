from Bio import SeqIO
from itertools import product
import pandas as pd
import argparse

# compare the headers of two FASTAs to provide content summaries

def register_arguments(parser):
    parser.add_argument('--input_fasta_1', '-1', dest="input_fasta_1", type=str,
                        help='First input FASTA to compare', required=True)
    parser.add_argument('--input-fasta_2', '-2', dest="input_fasta_2", type=str,
                        help='Second input FASTA to compare', required=True)
    parser.add_argument('--output-summary', '-o', dest="output_summary",
                        type=str, help='Optional output summary CSV file of '
                                       'header comparison', required=False)

def run(args):
    fasta_1_read = SeqIO.parse(open(args.input_fasta_1), 'fasta')
    fasta_2_read = SeqIO.parse(open(args.input_fasta_2), 'fasta')

    fasta_1_names = [record.name for record in fasta_1_read]
    fasta_2_names = [record.name for record in fasta_2_read]

    d = []

    for i, j in product(fasta_1_names, fasta_2_names):
        d.append([i, j])

    df = pd.DataFrame(d, columns=["fasta_1", "fasta_2"])

    same_entries = df[df.fasta_1 == df.fasta_2]

    # different_entries = df[df.fasta_1 != df.fasta_2]

    print("The following headers match in both input FASTAS:" + "\n")
    if same_entries.shape[0] > 0:
        print(same_entries.to_string(index=False))
        print("Number of matching FASTA sequences: {}".format(same_entries.shape[0]))
    else:
        print("No matching FASTA sequences were found between both input files")

    if args.output_summary:
        same_entries.to_csv(args.output_summary, index=False)

