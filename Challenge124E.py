# Tui Popenoe
# Challenge123E.py - Edge Sorting

import operator
import sys

def edgeSorting(lst):
    edges = list()
    for i in range(1, int(lst[0])):
        edges.push({
                'vert' : min(int(lst[i][1]), int(lst[i][2])
            })

    sorted_edges = sorted(edges, operator.itemgetter('vert'))

    print(sorted_edges)

def getInput(filename):
    f = open(filename, 'r')
    l = f.readlines()
    return l

def main():
    if len(sys.argv) > 1:
        edgeSorting(sys.argv[1])
    else:
        n = raw_input()
        l = list()
        for i in range(int(n)):
            j = int(raw_input().split())
            for k in j:
                l.append(k)
        edgeSorting(l)

if __name__=='__main__':
    main()

