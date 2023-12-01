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


def calibrate(lines):
    """Function that takes a list of strings and returns a list of calibration values
    corresponding to each string in the original list.

    The exercise defines "calibration values" as the sum of the first and last digits
    on a given line.

    If a line contains no digits, the assigned value is "None"
"""
    # Regular expression to see if string contains any digits
    RE_D = re.compile('\d')
    newlist = []
    for line in lines:
        digitmatch = RE_D.findall(line)
        print(line)
        print(digitmatch)
        if digitmatch:
            print(f'calval1 = {digitmatch[0]}, claval2 = {digitmatch[-1]}')
            calval = digitmatch[0] + digitmatch[-1]
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
