# Secret Santa

I wrote these commandline tools for myself to make it easier to run a Secret Santa event for my friends or coworkers

# Getting Started

- Download your responses spreadsheet as "responses.csv"
- Run get_names.py to generate the names file
- Run hat.py to get the shuffled pairs
- Run write_letters.py to create the assignment messages

# Known Issues

- Currently, write_letters.py requires ./output/letters to already exist and will fail with a file not found if it's not

# Future Work

- A nice wrapper around all the functionality with just one invocation target, having to run the three separate scripts is annoying
- Using a better CSV library like pandas or something
- #RIIR
