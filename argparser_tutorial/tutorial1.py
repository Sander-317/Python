import argparse
from rich import print

parser = argparse.ArgumentParser(description="print you input in the command line")
parser.add_argument("text", metavar="text", type=str, help="enter your text")
arg = parser.parse_args()

text = arg.text

print(text, 2)
