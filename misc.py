#PA 4

import re

"Miscellaneous functions to practice Python"

class Failure(Exception):
    """Failure exception"""
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

# Problem 1

# data type functions

"""
Problem 1a

This function uses the builtin abs to help
determine which number in a given list is closest
to the input number. Trivial subtraction takes
place to determine the absolute difference. 
"""
def closest_to(l, v):
    diff, c = None, None

    for n in l:
        if diff == None:
            diff = abs(v - n)
            c = n
        elif diff > abs(v - n):
            diff = abs(v - n)
            c = n

    return c

"""
Problem 1b

This fucntion returns a dictionary given a 
list of keys and values.
"""
def make_dict(keys, values):
    d = { }

    for i, v in enumerate(keys):
        d[v] = values[i]

    return d

"""
Problem 1c

This function finds all alphanumeric words (including _)
in a given line and file. I used the finall function of 
the regular expression module because it was easiest to 
adapt. The finall function allows me to break as string
with 'invalid' characters into a different 'tokens'. 
A dictionary is returned with the count of each unique string.
"""
def word_count(file_name):
    d = { }
    f = open(file_name, 'r')
    for line in f:
        tokens = re.findall('([A-Za-z0-9_]+)', line)   
        tokens = [x.lower() for x in tokens]
        for token in tokens:
            if d.has_key(token) == False:
                d[token] = 1
            else:
                d[token] = d[token] + 1
    return d





