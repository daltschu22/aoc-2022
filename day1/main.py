#!/usr/bin/env python

# Written by daltschu22 -- https://github.com/daltschu22

import sys


def main():

    # Get the input file
    input_file = sys.argv[1]

    # Open the input file
    with open(input_file, 'r') as f:
        # Read the file
        data = f.readlines()

    elf_totals = {}

    # Loop through the data
    calories = []
    elf_counter = 1
    for line in data:
        if line.strip() == "":
            sub_cal = calories.copy()
            calories.clear()
            total = sum(sub_cal)

            elf_totals[elf_counter] = total
            elf_counter += 1
        else:
            calories.append(int(line.strip()))

    max_elf = max(elf_totals, key=elf_totals.get)

    sorted_elves = sorted(elf_totals.values(), reverse=True)

    elf1 = sorted_elves[0]
    elf2 = sorted_elves[1]
    elf3 = sorted_elves[2]

    top_3 = elf1 + elf2 + elf3

    print(top_3)


if __name__ == '__main__':
    main()
