import argparse
import re
import os
import sys
import importlib
from types import SimpleNamespace
from argparse import RawTextHelpFormatter


command_strings = ["gisaid", "nextstrain", "composition", "filter", "subset"]

COMMANDS = [importlib.import_module('fastafurious.' + c) for c in command_strings]

print(commands)

