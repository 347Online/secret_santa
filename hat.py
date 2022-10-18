#!/usr/bin/env python3

import argparse
from pathlib import Path
import random
import math
import json

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--names", help = "name of the file to use as the list of participants", default = "names.txt")
parser.add_argument("-v", "--verbose", action = "store_true")
args = parser.parse_args()

def derange(ls) -> list:
  l = ls.copy()
  length = len(l)
  for i in range(length - 1):
    j = i + 1 + math.floor(random.random() * (length - i - 1))
    l[i],l[j] = l[j],l[i]
  return l

def create_pairs(l) -> dict:
  shuffle = derange(l.copy())
  return dict(zip(l, shuffle))
  

def print_pairs(d) -> None:
  for key in d:
    print(key.ljust(24) + d[key])
    

def main() -> None:
  try:
    with open(args.names) as f:
      names = f.read().splitlines()
      pairs = create_pairs(names)
      if args.verbose:
        print_pairs(pairs)

  except IOError:
    print(f"Could not open '{args.names}'")
  
  try:
    fname = Path(args.names).stem + ".json"
    with open(fname, "w") as f:
      f.write(json.dumps(pairs))

  except IOError:
    print(f"Could not write file '{fname}'")
  

if __name__ == "__main__":
  main()