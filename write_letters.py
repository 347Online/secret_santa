#!/usr/bin/env python3

# Generates the messages informing participants of who their assigned recipient is

# Hello {PARTICIPANT}

# Your recipient is {RECIPIENT}

# Their survey responses were {RESPONSES}

import json
import csv
from pathlib import Path

def write_letter(p, r, q):
  response_string = ""
  for key, value in q.items():
    if key == "Discord Handle":
      continue
    response_string += key + ":\n" + value + "\n\n"

  letter = f"""Seasons greetings, {p}!

Your assigned recipient is {r}, here are their questionnaire responses:

{response_string}
Once again, thank you so much for participating in Secret Santa this year!

Happy Holidays!!"""
  
  return letter



def main():

  with open("output/names.json") as f:
    people = json.load(f)
  
  responses = {}
  with open("responses.csv") as r:
    for line in csv.DictReader(r):
      name = line["Preferred Name"]
      responses[name] = line

  for participant, recipient in people.items():
    response_dict = responses[recipient]

    letter = write_letter(participant, recipient, response_dict)
    with open("output/letters/" + participant + ".txt", "w+") as f:
      f.write(letter)

if __name__ == "__main__":
  main()