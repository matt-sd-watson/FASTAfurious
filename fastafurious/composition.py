from Bio import SeqIO
import argparse


def register_arguments(parser):
    parser.add_argument('--input_fasta', '-i', type=str, help='input multi-FASTA to verify', required=True)
    parser.add_argument('--length', '-l', type=float, help='Minimum length for each record in the '
                                                           'multi-FASTA', default=29700)
    parser.add_argument('--completeness', '-c', type=float, help='Minimum genome completeness percent for each record '
                                                                 'in the multi-FASTA', default=90)


def run(args):

    fasta_sequences = SeqIO.parse(open(args.input_fasta), 'fasta')

    too_short = 0
    for record in fasta_sequences:
        if len(record) < args.length:
            too_short += 1
            print("WARNING: The following sequences are too short for analysis: Sequence: {}, Length: {}".format(record.name, len(record)))
        try:
            genome_completeness = 100 - (100 * record.seq.count("N") / len(record))
            if genome_completeness < args.completeness:
                print("WARNING: The following sequences have genome completeness below {}%: {}  {}".format(
                    args.completeness, record.name, genome_completeness))
        except ZeroDivisionError:
            print("WARNING: sequence does not have any length: {}".format(record.name) + "\n")
    if too_short == 0:
        print("All sequences are long enough for analysis")
