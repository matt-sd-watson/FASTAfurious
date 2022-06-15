_program = "fastafurious"
__version__ = "1.2.4"

import argparse
import re
import os
import sys
import importlib
from types import SimpleNamespace
from argparse import RawTextHelpFormatter


# make a dictionary with sub-commands and their descriptions
help_dict = {"filter": "filter sequences in FASTA based on completeness and length",
             "composition": "Print the composition statistics of FASTA sequences (completeness/length)",
             "subset": "Create a FASTA subset based on a txt list or bash record input",
             "rename": "Rename the headers of a fasta file based on the columns of a CSV file",
             "compare": "Compare the header entries of two FASTA input files",
             "version": "Print the current FASTAfurious version then exit."}

command_dict = {}
for command in help_dict.keys():
    command_dict[str(importlib.import_module('fastafurious.' + str(command)))] = command

# import the modules for each of the subcommands
# requires the names of the modules to be named the same as the subcommand
COMMANDS = [importlib.import_module('fastafurious.' + c) for c in help_dict.keys()]


def first_line(text):
    """
    Returns the first line of the given text, ignoring leading and trailing
    whitespace.
    """
    return text.strip().splitlines()[0]


def make_parser():
    parser = argparse.ArgumentParser(
        prog="fastafurious",
        description="fastafurious: Bundled utilities for manipulating and integrating FASTA files",
        formatter_class=RawTextHelpFormatter)

    subparsers = parser.add_subparsers(description="fastafurious provides a series of bundled functions to \n"
                                                   "easily manipulate and integrate FASTA FILES into routine \n"
                                                   "bioinformatics workflows")

    add_default_command(parser)
    # add_version_alias(parser)

    # create a unique sub-parser for each of the possible sub commands
    # requires the sub commands to have register_arguments and run commands in the script file
    for command in COMMANDS:

        # add the help description for each sub commands to its subparser
        help_line = help_dict.get(command_dict.get(str(command)))
        subparser = subparsers.add_parser(command_name(command), help=help_line,
                                              description=help_line)

        subparser.set_defaults(__command__=command)

        # Let the command register arguments on its subparser.
        command.register_arguments(subparser)

        # Use the same formatting class for every command for consistency.
        # Set here to avoid repeating it in every command's register_parser().
        subparser.formatter_class = argparse.ArgumentDefaultsHelpFormatter

    return parser


def run(argv):
    args = make_parser().parse_args(argv)
    return args.__command__.run(args)


def add_default_command(parser):
    """
    Sets the default command to run when none is provided.
    """

    class default_command():
        def run(args):
            parser.print_help()
            return 2

    parser.set_defaults(__command__ = default_command)


def command_name(command):
    """
    Returns a short name for a command module.
    """

    def remove_prefix(prefix, string):
        return re.sub('^' + re.escape(prefix), '', string)

    package = command.__package__
    module_name = command.__name__

    return remove_prefix(package, module_name).lstrip(".").replace("_", "-")


