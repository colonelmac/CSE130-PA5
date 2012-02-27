
from misc import *
import crypt

def load_words(filename, regexp):
    l = [ ]
    f = open(filename, 'r')
    for line in f:  
      item = re.match(regexp, line)
      if item != None:
        l.append(line[item.start():item.end()])
    return l

def transform_reverse(s):
    st = ''
    for x in reversed(s):
      st += x
    return [s, st] 

def transform_capitalize(string):
  words = [] 
  capitalize_helper(string, "", words)
  return words

def capitalize_helper(string, previous, words):
  if len(string) == 1: 
    words.append(previous + string.upper())
    words.append(previous + string.lower())
    return words
  capitalize_helper(string[1:], previous + string[0:1].upper(), words)
  capitalize_helper(string[1:], previous + string[0:1].lower(), words)

def tc(string):
    string = string.lower()
    if len(string) > 1:
      res = tc(s[1:])
      return (s[0:1].upper() + res[0], s[0:1].lower() + res[1])
    else:
      return (string.upper(), string.lower())

def transform_digits(str):
    raise Failure("to be written")

def check_pass(plain,enc):
    """Check to see if the plaintext plain encrypts to the encrypted
       text enc"""
    raise Failure("to be written")

def load_passwd(filename):
    """Load the password file filename and returns a list of
       dictionaries with fields "account", "password", "UID", "GID",
       "GECOS", "directory", and "shell", each mapping to the
       corresponding field of the file."""
    raise Failure("to be written")

def crack_pass_file(fn_pass,words,out):
    """Crack as many passwords in file fn_pass as possible using words
       in the file words"""
    raise Failure("to be written")

