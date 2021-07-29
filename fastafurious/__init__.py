_program = "fastafurious"
__version__ = "1.0.0"

import argparse
import re
import os
import sys
import importlib
from types import SimpleNamespace
from argparse import RawTextHelpFormatter

# specify the sub-commands available
command_strings = ["gisaid", "nextstrain", "composition", "filter", "subset"]

# make a dictionary with sub-commands and their descriptions
help_dict = {"filter": "filter sequences in FASTA based on completeness and length",
             "gisaid": "Rename FASTA headers to be compatible with Gisaid submissions",
             "nextstrain": "Rename FASTA hedaers to be compatible with Nextstrain builds",
             "composition": "Print the composition statistics of FASTA sequences",
             "subset": "Create a FASTA subset based on a txt list of bash record list"}


# import the modules for each of the subcommands
# requires the names of the modules to be named the same as the subcommand
COMMANDS = [importlib.import_module('fastafurious.' + c) for c in command_strings]


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
        # add the help dscription for each sub commands to its subparser
        if str(command).split('fastafurious.')[1].split("\'")[0] in help_dict:
            help_line = help_dict.get(str(command).split('fastafurious.')[1].split("\'")[0])
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

