#! /usr/bin/python3
import argparse
import re
import numpy as np

def read_as_list(filename):
    """Function to read text document and return as a list of strings

    Args:
        filename (str): The full or relative path of the filename to be read

    Returns:
        list: List of lines from opened file
    """


    with open(filename) as f:
        l = f.read().splitlines()

    return l


def put_results_in_list(s):
    """Given a string indicating the number of red, green, and/or blue in a given draw,
    outputs a list of the form (red, green, blue) indicating the results"""

    red = re.findall(r'\d+ red',s)
    green = re.findall(r'\d+ green',s)
    blue = re.findall(r'\d+ blue',s)

    draw = [0, 0, 0]

    print(f"String: {s}")

    if red:
        print(f"in red {red[0]}")
        draw[0]=int(re.findall(r'\d+', red[0])[0])
    if green:
        draw[1]=int(re.findall(r'\d+', green[0])[0])
    if blue:
        draw[2]=int(re.findall(r'\d+', blue[0])[0])

    print(draw)
    return draw


def parse_results(string,v=False):
    """Function that takes a string and outputs a list of lists of game results

    Each draw is an entry in the list, and each sub-list enumerates the number of red, 
    green, and blue cubes for a given draw

    Second optional argument is a verbose flag
"""

    draw = []

    string = string.split(": ")

    strings = string[1].split("; ")

    for s in strings:
        thisdraw = put_results_in_list(s)
        draw.append(thisdraw)
        if v:
            print(f"{string[0]} {thisdraw}")

    return draw


def verify(gamelist,load):
    """Function that takes a list of list from one game, as well as the true load of the bag,
    and returns True if that game was possible, False otherwise
"""

    print(gamelist)

    for picklist in gamelist:
        #Check reds
        print(picklist)
        print(load)
        if picklist[0] > load[0]:
            return False
        #Check greens
        if picklist[1] > load[1]:
            return False
        #Check blues
        if picklist[2] > load[2]:
            return False

    return True

def find_min_set(gamelist):
    """Given a game list, returns the minimum load possible for that game"""

    minset = [0,0,0]

    i=0
    print(gamelist)
    for game in gamelist:
        if minset[0] < game[0]:
            minset[0] = game[0]
        if minset[1] < game[1]:
            minset[1] = game[1]
        if minset[2] < game[2]:
            minset[2] = game[2]

        i+=1


    return minset

def main():
    """Main function for Advent of code: day 2"""

    #Parse arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--filename', type=str, help='filename to read', required=True)
    parser.add_argument('-l', '--load', type=list, help='The true load of cubes in the bag (list of form [red, green, blue])', default=[12,13,14])
    parser.add_argument('-v', '--verbose', action='store_true')
    pargs = parser.parse_args()

    lines = read_as_list(pargs.filename)

    results = []
    sumpower = 0
    for line in lines:
        result = parse_results(line,pargs.verbose)
        results.append(result)

        minset = find_min_set(result)

        power = np.prod(minset)
        print(f"For {line}\n{minset=}\n{power=}")

        sumpower += power


    print(f"Sum of all powers: {sumpower}")

    # Now verify results

#    i=j=0
#    for result in results:
#        i+=1
#        if verify(result,pargs.load):
#            if pargs.verbose:
#                print(f"Game {i} was possible!")
#            j += i
#        else:
#            if pargs.verbose:
#                print(f"Game {i} was impossible!")
#
#    print(f"Sum of possible IDs is {j=}")



if __name__ == "__main__":
    main()
