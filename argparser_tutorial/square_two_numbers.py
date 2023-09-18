from argparse import ArgumentParser, Namespace
from rich import print

parser = ArgumentParser()
group = (
    parser.add_mutually_exclusive_group()
)  # groups are to make sure you cant pick 2 options that dont go to gether

parser.add_argument("firstNumber", type=int, help="This is the base value")
parser.add_argument("secondNumber", type=int, help="This is the exponent value")
group.add_argument(
    "-v",
    "--verbose",
    action="count",  # counts the number of argument example = -vv or --verbose --verbose
    help="Provides a verbose description. Use -vv for extra verbose version",
)
group.add_argument(
    "-s",
    "--silence",
    action="store_true",  # stores True or False flags
    help="Generate a silent version of the output.",
)

args: Namespace = parser.parse_args()
result: int = args.firstNumber**args.secondNumber

if args.silence:
    print("Silenced!")
else:
    match args.verbose:
        case 1:
            print(f"The result is {result}")
        case 2:
            print(f"{args.firstNumber} ** {args.secondNumber} = {result}")
        case _:
            print(result)
