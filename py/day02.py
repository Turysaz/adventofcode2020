
# Advent of code 2020, day 02
#
# Tasks:
# Part 1: Read all the lines from the file. Each line specifies a range R, a
#         character C and a password P. P is valid if the number of Cs in it is
#         within R.
# Part 2: P is only valid if it contains a C at exactly one of the limits of R.
#

import re

with open("../inputs/day02.txt") as file:
    lines = file.readlines()

pattern = "(?P<n1>\d+)-(?P<n2>\d+) (?P<sym>\w): (?P<pw>\w+)"

def part1():
    valid_c = 0
    for l in lines:
        m = re.match(pattern, l)
        min, max, sym, pw = m.group("n1", "n2", "sym", "pw")
        min, max = int(min), int(max)
        if pw.count(sym) < min or pw.count(sym) > max:
            continue

        valid_c += 1

    print("Part 1: {}".format(valid_c))

def part2():
    valid_c = 0
    for l in lines:
        m = re.match(pattern, l)
        i1, i2, sym, pw = m.group("n1", "n2", "sym", "pw")
        i1, i2 = int(i1)-1, int(i2)-1 # adjusting indices
        if (pw[i1] == sym) != (pw[i2] == sym):
            valid_c += 1
            continue

    print("Part 2: {}".format(valid_c))


part1()
part2()

