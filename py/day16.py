
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

    rules, own_ticket, other_tickets = parse(lines)

    valid_tix = [] # entries represent the matches for one ticket, each.
    error_rate = 0
    other_tickets.append(own_ticket)
    for ticket in other_tickets:
        field_matches = []
        error, errorcode = False, 0
        for candidate in ticket:
            applying_rules = set(r.name for r in rules if r.okay(candidate))
            if len(applying_rules) == 0:
                error = True
                errorcode += candidate
            field_matches.append(applying_rules)
        error_rate += errorcode
        if not error:
            valid_tix.append(field_matches)

    print("Part 1: %i" % error_rate)

    candidates=[]
    for i in range(len(rules)):
        candidates.append(list(set.intersection(*[t[i] for t in valid_tix])))

    field_indices = {}
    while (candidate := next(filter(lambda x: len(x) == 1, candidates), False)):
        field_name = candidate[0]
        field_indices[candidates.index(candidate)] = field_name
        for c in candidates:
            if field_name in c:
                c.remove(field_name)

    product = 1
    for i in field_indices:
        if field_indices[i].startswith("departure"):
            product *= own_ticket[i]

    print("Part 2: %i" % product)
