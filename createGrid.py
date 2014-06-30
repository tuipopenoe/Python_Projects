# Tui Popenoe
# createGrid 
"""Python utility to create a grid of the given character, X * Y"""

import sys

def createGrid(x, y, char='0'):
    grid = [[char for i in xrange(x)] for j in xrange(y)]
    return grid

def main():
    createGrid(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__=='__main__':
    main()