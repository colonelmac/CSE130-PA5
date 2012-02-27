
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

def transform_digits(string):
  words = [] 
  digits_helper(string, "", words)
  return words

def digits_helper(string, previous, words):
  if len(string) == 1: 
    words.append(previous + swap_char(string))
    return words
  if(string[0:1] == "B"):
    digits_helper(string[1:], previous + swap_char(string[0:1].lower()), words)
  digits_helper(string[1:], previous + swap_char(string[0:1]), words)
  digits_helper(string[1:], previous + string[0:1], words)

def swap_char(c):
  d = {
    "o": 0,
    "i": 1,
    "l": 1,
    "z": 2,
    "e": 3,
    "a": 4,
    "s": 5,
    "t": 7,
    "b": 6,
    "B": 8
  }

  return str(d.get(c)) if d.get(c) != None else c

def check_pass(plain, enc):
  return enc == crypt.crypt(plain, enc[0:2])

def load_passwd(filename):
  dicts = [ ]
  f = open(filename)
  for line in f:
    tmp = { }
    for i, token in enumerate(re.split(":", line)):
      tmp[i] = token.rstrip('\n')
    dicts.append(replace_keys(tmp))
  return dicts

def replace_keys(d):
  tmp = { }
  tmp["account"]    = d[0]
  tmp["password"]   = d[1]
  tmp["UID"]        = d[2]
  tmp["GID"]        = d[3]
  tmp["GECOS"]      = d[4]
  tmp["directory"]  = d[5]
  tmp["shell"]      = d[6]
  return tmp

def crack_pass_file(password_file, words_file, output_file):
  users = load_passwd(password_file)
  words = load_words(words_file, r"([A-Za-z0-9_]+)$")

  reverse = [transform_reverse(w)[1] for w in words]
  #capital = [transform_capitalize(w) for w in words]
  #digit   = [transform_digits(w) for w in words]

  out   = open(output_file, 'w')

#capital = [transform_capitalize(w) for w in words]

  #print users

  for i, word in enumerate(words):
    for j, user in enumerate(users):
    
      if check_pass(word, user["password"]):
        out.write(user["account"] + ":" + word + "\n")
        del users[j]
        break
      
      if check_pass(reverse[i], user["password"]):
        out.write(user["account"] + ":" + reverse[i] + "\n")
        out.flush()
        del users[j]
        break

  del reverse

  out.close()
  return
  """
  for word in words:
    if len(users) > 0:
      for cap in transform_capitalize(word):
        for j, user in enumerate(users):

          if check_pass(cap, user["password"]):
            out.write(user["account"] + ":" + cap + "\n")
            out.flush()
            del users[j]
            break

  for word in words:
    if len(users) > 0:
      for dig in transform_digits(word):
        for j, user in enumerate(users):

          if check_pass(dig, user["password"]):
            out.write(user["account"] + ":" + dig + "\n")
            out.flush()
            del users[j]
            break    

            """    