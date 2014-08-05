# Tui Popenoe
# utils.py 
""" A bunch of python utilities I've used over the years. """

import os
import sys

def reverse_string(string):
    """ Uses the extended slice syntax [begin:end:step] omitting beginning and
    end and specifying a step of -1. """
    return string[::-1]

def most_common_element(lst):
    """ Returns the most common element in a list. """
    return max(set(lst), key=lst.count)

def remove_char_from_list(lst):
    """ Remove all instances of a character from a list. """
    return map(lambda s: s.strip(), lst)

def convert_file_to_list(filename):
    """ Converts a file to list. """
    lst = [i.strip().split() for i in open(filename).readlines()]
    l = [item for sublist in lst for item in sublist]
    f = open(filename, 'w')
    f.write('\n'.join(map(lambda x: str(x), l)))
    f.close()

def get_full_filepath(filename):
    """ Returns a tuple of the path and the full pathname of the given 
    filename. """
    pathname = os.path.dirname(filename)
    return ('filename = ' + filename, 'path = ' + pathname, \
        'full path = ' + os.abspath(pathname))
