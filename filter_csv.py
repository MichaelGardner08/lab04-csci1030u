# Part 2 (STRETCH) - filter the rows of a CSV file.
#
# This is a COMMAND-LINE program. You run it like:
#     python filter_csv.py people.csv city Oshawa

import argparse
import csv


def main():
    parser = argparse.ArgumentParser(
        description="Print the rows of a CSV where a column has a given value.")
    parser.add_argument("filename", help="the CSV file to read")
    parser.add_argument("column", help="the name of the column to match on")
    parser.add_argument("value", help="the value to match")

    args = parser.parse_args()

    # Open the CSV file and read all rows
    with open(args.filename, newline="") as file:
        rows = list(csv.reader(file))

    # The first row contains the column names
    header = rows[0]
    column_index = header.index(args.column)

    # Print rows where the chosen column matches the value
    for row in rows[1:]:
        if row[column_index] == args.value:
            print(",".join(row))


if __name__ == "__main__":
    main()
