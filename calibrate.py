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

    #Pad string with spaces to avoid complications when matching "string numbers" later
    string = string + "     "

    for i, v in enumerate(string[0:-5]):
        if v.isdigit():
            digits.append(v)
        elif string[i:i+3] == 'one':
            digits.append(1)
        elif string[i:i+3] == 'two':
            digits.append(2)
        elif string[i:i+5] == 'three':
            digits.append(3)
        elif string[i:i+4] == 'four':
            digits.append(4)
        elif string[i:i+4] == 'five':
            digits.append(5)
        elif string[i:i+3] == 'six':
            digits.append(6)
        elif string[i:i+5] == 'seven':
            digits.append(7)
        elif string[i:i+5] == 'eight':
            digits.append(8)
        elif string[i:i+4] == 'nine':
            digits.append(9)
        elif string[i:i+4] == 'zero':
            digits.append(0)

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
            calval = str(dm[0]) + str(dm[-1])
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
