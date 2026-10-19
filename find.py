# Part 1 - a small "find" tool (like a simplified "grep").
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")

    # Add the optional ignore-case flag
    parser.add_argument("-i", "--ignore-case", action="store_true")

    args = parser.parse_args()

    # Open the file and search each line
    with open(args.filename) as file:
        for number, line in enumerate(file, start=1):
            # Remove the trailing newline
            line = line.rstrip("\n")

            # Match with or without case sensitivity
            if args.ignore_case:
                match = args.pattern.lower() in line.lower()
            else:
                match = args.pattern in line

            if match:
                print(f"{number}: {line}")


if __name__ == "__main__":
    main()
