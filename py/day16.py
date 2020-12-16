
# Advent of code 2020, day16
#
# Tasks:
# Part 1: In sets of numbers, find numbers that do not match any of the given
#         rules (ranges) and return the sum of them.
#

import re

class Rule():
    __pattern = r"(?P<n>[\w ]*): (?P<l1>\d*)-(?P<r1>\d*) or (?P<l2>\d*)-(?P<r2>\d*)"

    def __init__(self, string):
        m = re.match(self.__pattern, string)
        self.name = m.group("n")
        self._l1 = int(m.group("l1"))
        self._r1 = int(m.group("r1"))
        self._l2 = int(m.group("l2"))
        self._r2 = int(m.group("r2"))
    
    def okay(self, number: int) -> bool:
        return (self._l1 <= number and number <= self._r1
                or self._l2 <= number and number <= self._r2)

def parse(lines: list[str]) -> tuple[list[Rule], list[int], list[list[int]]]:
    """
    Returns a tuple of all rules, then the own ticket, then all other tickets.
    """
    rules=[]
    own_ticket = None
    other_tickets = []
    i = 0
    while lines[i] != "":
        rules.append(Rule(lines[i]))
        i+=1
    own_ticket = [int(x) for x in lines[i+2].split(",")]
    i += 5
    while i < len(lines):
        other_tickets.append([int(x) for x in lines[i].split(",")])
        i+=1
    return (rules, own_ticket, other_tickets)


if __name__ == "__main__":
    with open("../inputs/day16.txt") as file:
        lines = file.read().splitlines(keepends=False)

    lines_d = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".splitlines(keepends=False)

    lines_d = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".splitlines(keepends=False)


    rules, own_ticket, other_tickets = parse(lines)

    matches = [] # entries represent the matches for one ticket, each.
    error_rate = 0
    for ticket in other_tickets:
        field_matches = []
        error = 0
        for field in ticket:
            applying_rules = set(r.name for r in rules if r.okay(field))
            if len(applying_rules) == 0:
                error += field
            field_matches.append(applying_rules)
        error_rate += error
        if error == 0:
            matches.append(field_matches)

    print("Part 1: %i" % error_rate)

