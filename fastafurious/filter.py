from Bio import SeqIO
import argparse


def register_arguments(parser):
    parser.add_argument('--input_fasta', '-i', type=str, help='input multi-FASTA to verify', required=True)
    parser.add_argument('--length', '-l', type=float, help='Minimum length for each record in the '
                                                           'multi-FASTA', default=29700)
    parser.add_argument('--completeness', '-c', type=float, help='Minimum genome completeness percent for each record '
                                                                 'in the multi-FASTA', default=90)
    parser.add_argument('--output_fasta', '-o', type=str, help='output FASTA containing clean records',
                        default='cleaned.fasta')


def run(args):

    fasta_sequences = SeqIO.parse(open(args.input_fasta), 'fasta')

    count = 0
    with open(args.output_fasta, "w") as handle:
        for record in fasta_sequences:
            try:
                genome_completeness = 100 - (100 * record.seq.count("N") / len(record))
                if len(record) > args.length and genome_completeness >= args.completeness:
                    count += 1
                    SeqIO.write(record, handle, "fasta")
            except ZeroDivisionError:
                if len(record) > args.length:
                    count += 1
                    SeqIO.write(record, handle, "fasta")
                    print("WARNING: Adding record with length 0, completeness could not be calculated: {}".
                          format(record.name))

    print("{} sequences written to {}".format(count, args.output_fasta))
