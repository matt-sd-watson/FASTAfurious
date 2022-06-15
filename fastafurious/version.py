from fastafurious import __version__
import argparse
import sys

def register_arguments(parser):
    parser.add_argument('-v', "--version", action="version",
                        help="Show the current FASTAfurious version then exit.",
                        version=f"This is FASTAfurious: v{__version__}")

def run(args):
    print("This is FASTAfurious: v{}".format(__version__))
    sys.exit(0)
