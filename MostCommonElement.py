# Tui Popenoe
# MostCommonElement.py

def mostCommon(lst):
    return max(set(lst), key=lst.count)