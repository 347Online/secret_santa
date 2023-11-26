#!/usr/bin/env python3
import csv
from pathlib import Path

names = []
with open("responses.csv") as responses:
  for line in csv.DictReader(responses):
    names.append(line["Preferred Name"])

with open("names.txt", "w") as names_file:
  names_file.writelines("\n".join(names))
  names_file.write("\n")