# Do not modify these lines
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Add your code after this line
import sys
import argparse
from rich.traceback import install

install(show_locals=True)


def main():
    parser = argparse.ArgumentParser(description=" welcome stds in out and err")
    parser.add_argument(
        "input",
        metavar="input",
        type=str,
        nargs="?",
        help="give input",
    )
    arg = parser.parse_args()
    input = arg.input

    # TODO: read text from stdin
    text = sys.stdin.read()

    # TODO: Filter character given as an argument from the text
    new_text = text.replace(input, "")

    # TODO: Print the result to stdout
    sys.stdout.write(new_text)

    # TODO: Print the total number of removed characters to stderr
    sys.stderr.write(str(len(text) - len(new_text)))

    ...


if __name__ == "__main__":
    main()
