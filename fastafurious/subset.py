# !/usr/bin/env python
# faSomeRecords.py

import argparse
import textwrap
import sys


def register_arguments(parser):
    parser.add_argument('--fasta', '-f', metavar='FASTA_FILE', type=str, required=True,
                        help='FASTA file where all the sequences are stored.')
    parser.add_argument('--list', '-l', metavar='LIST', type=str, help='file name of the list.')
    parser.add_argument('--records', '-r', metavar='RECORD', nargs="*", type=str, help='individual FASTA records.')
    parser.add_argument('--outfile', '-o', default="records.fasta", nargs="?", type=str,
                        help='name for output file (default: %(default)s)')
    parser.add_argument('--stdout', '-s', action="store_true", default=False,
                        help='if sequences should be printed to screen.')
    parser.add_argument('--keep', '-k', action="store_true", default=False, help="keep the order in the list.")
    parser.add_argument('--exclude', '-e', action="store_true", default=False,
                        help="Exclude these sequences from the final output.")


def run(args):

    if args.list is None and args.records is None:
        # parser.print_usage()
        sys.exit("FaSomeRecords.py: error: argument --list/-l or --records/-r is required")
    if args.list is not None and args.records is None:
        with open(args.list, "r") as l:
            heads = l.read().splitlines()
        if ">" not in heads[0]:
            heads = [">" + h for h in heads]
    elif args.records is not None and args.list is None:
        heads = args.records
        if ">" not in heads[0]:
            heads = [">" + h for h in heads]

    requested = len(heads)
    joinheads = "|" + "|".join(heads) + "|"

    found = 0
    not_found = []

    if args.exclude:
        if args.keep:
            print("--exclude will maintain the order of the original FASTA by default")
        with open(args.outfile, "w") as out:
            with open(args.fasta, "r") as f:
                for line in f:
                    if line.startswith(">") and line.strip("\n") not in heads:
                        seq = 1
                        out.write(line)
                        found += 1
                    elif line.startswith(">"):
                        not_found += [line[1:-1]]
                        seq = 0
                    else:
                        if seq == 1:
                            out.write(line)

    elif args.keep and not args.exclude:
        store = {}
        with open(args.fasta, "r") as f:
            for line in f:
                if line[0] == ">":
                    if "|" + line[:-1] + "|" in joinheads:
                        h = line[:-1]
                        seq = 1
                        store[h] = ''
                        found += 1
                    else:
                        seq = 0
                else:
                    if seq == 1:
                        store[h] += line
        if found == 0:
            print("No sequences found")
        else:
            if args.stdout:
                for h in heads:
                    if store.get(h):
                        sys.stdout.write(h + "\n" + store[h])
                    else:
                        sys.stdout.write(h + "\n" + "#not found\n")
                        not_found += [h]
            else:
                with open(args.outfile, "w") as o:
                    for h in heads:
                        if store.get(h):
                            o.write(h + "\n" + store[h])
                        else:
                            sys.stdout.write(h + "\n" + "#not found\n")
                            not_found += [h]
                print("Found {} sequence(s)".format(found))
                if found > requested:
                    print("Found {} sequence(s) more than requested".format(found - requested))
                elif requested > found:
                    print("Could not find {} sequence(s)".format(requested - found))
                    print("\n".join(not_found))
                print("Sequences saved to: " + args.outfile)
    else:
        if args.stdout:
            with open(args.fasta, "r") as f:
                for line in f:
                    if line[0] == ">":
                        if "|" + line[:-1] + "|" in joinheads:
                            seq = 1
                            sys.stdout.write(line)
                            found += 1
                        else:
                            not_found += [line[:-1]]
                            seq = 0
                    else:
                        if seq == 1:
                            sys.stdout.write(line)
            if found == 0:
                print("No sequences found")
        else:
            with open(args.outfile, "w") as o:
                with open(args.fasta, "r") as f:
                    for line in f:
                        if line[0] == ">":
                            if "|" + line[:-1] + "|" in joinheads:
                                seq = 1
                                o.write(line)
                                found += 1
                            else:
                                not_found += [line[1:-1]]
                                seq = 0
                        else:
                            if seq == 1:
                                o.write(line)
            if found == 0:
                print("No sequences found")
            else:
                print("Found {} sequence(s)".format(found))
                if found > requested:
                    print("Found {} sequence(s) more than requested".format(found - requested))
                elif requested > found:
                    print("Could not find {} sequence(s)".format(requested - found))
                    print("\n".join(not_found))
                print("Sequences saved to " + args.outfile)