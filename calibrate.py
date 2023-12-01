#! /usr/bin/python3
import argparse
import re

def read_as_list(filename):
    """Function to read calibration document and return as a list of strings

    Args:
        filename (str): The full or relative path of the filename to be read

    Returns:
        list: List of lines from opened file
    """


    with open(filename) as f:
        l = f.read().splitlines()

    return l

def digitmatch(string):
    """Function that takes a string and outputs a list of all "digits" in that string.

    For the purpose of this function, a digit is either a numerical character:
    0 1 2 3 4 5 6 7 8 9

    Or the name of a single-digit number:

    zero one two three four five six seven eight nine
"""

    digits = []

    for i, v in enumerate(string):
        if v.isdigit():
            print(v)
            digits.append(v)

    return digits


def calibrate(lines):
    """Function that takes a list of strings and returns a list of calibration values
    corresponding to each string in the original list.

    The exercise defines "calibration values" as the sum of the first and last digits
    on a given line.

    If a line contains no digits, the assigned value is "None"
"""
    # Regular expression to see if string contains any digits
    newlist = []
    for line in lines:
        dm = digitmatch(line)
        if dm:
            calval = dm[0] + dm[-1]
            newlist.append(int(calval))
        else:
            newlist.append(None)

    return newlist

def main():
    """Main function for Advent of code: day 1"""

    #Parse arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--filename', type=str, help='filename to read', required=True)
    pargs = parser.parse_args()

    lines = read_as_list(pargs.filename)

    cals = calibrate(lines)

    print("Calibration values:")
    print(cals)

    print(f'calibration total: {sum(cals)}')

if __name__ == "__main__":
    main()
