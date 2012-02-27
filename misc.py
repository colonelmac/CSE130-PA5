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

def make_dict(keys, values):
    d = { }

    for i, v in enumerate(keys):
        d[v] = values[i]

    return d

# file IO functions
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





