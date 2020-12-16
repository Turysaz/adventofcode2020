
# Advent of code 2020, day16
#
# Tasks:
# Part 1: In sets of numbers, find numbers that do not match any of the given
#         rules (ranges) and return the sum of them.
# Part 2: Determine which position of numbers must be which field and then
#         multiply together all numbers from the own ticket that belong to
#         fields that start with "departure".
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
    "Returns a tuple of all rules, then the own ticket, then all other tickets."
    rules, own_ticket, other_tickets = [], None, []
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

    valid_tickets = [] # entries represent the matches for one ticket, each.
    error_rate = 0
    for ticket in other_tickets:
        applying_rules_for_fields = []
        error, errorcode = False, 0
        for number in ticket:
            applying_rules = set(r.name for r in rules if r.okay(number))
            if len(applying_rules) == 0:
                error = True
                errorcode += number
            applying_rules_for_fields.append(applying_rules)
        error_rate += errorcode
        if not error:
            valid_tickets.append(applying_rules_for_fields)

    print("Part 1: %i" % error_rate)

    product = 1
    candidates = [list(set.intersection(*[t[i] for t in valid_tickets]))
                  for i in range(len(rules))]
    # iteratively remove the unambigous field from all sets to reduce the
    # number of possibilities
    while (candidate := next(filter(lambda x: len(x) == 1, candidates), False)):
        name = candidate[0]
        product *= (own_ticket[candidates.index(candidate)]
                    if name.startswith("departure") else 1)
        for c in candidates:
            if name in c:
                c.remove(name)

    print("Part 2: %i" % product)
