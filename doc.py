import argparse
import os

parser = argparse.ArgumentParser(
description = "Displays the documentation of a Python keyword",
usage = "doc [keyword]")
parser.add_argument("kw",  help="source_folder")
args = parser.parse_args()

os.system("python -m pydoc %s" % (args.kw))