# Tui Popenoe
# createGrid 
"""Python utility to create a grid of the given character, X * Y
    createGrid -e 10 10 x to create a 10x10 grid of x character.
    createGrid -f to crate a grid from an input file"""

import sys

def createEmptyGrid(x, y, char='0'):
    grid = [[char for i in xrange(x)] for j in xrange(y)]
    return grid

def creatGridFromFile(filename):
    f = open(filename, 'r')
    grid = list()
    for line in list:
        grid.append([])
        for char in line:
            grid[line].append(char):

    f.close()

    return grid

def main():
    if sys.argv[1] == '-e':
        createEmptyGrid(sys.argv[2,3,4])
    elif sys.argv[1] == '-f':
        createGridFromFile(sys.argv[2])

if __name__=='__main__':
    main()