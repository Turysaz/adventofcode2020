
# Advent of code 2020, day 06
#
# Tasks:
# Part 1: Given a set of groups of characters, find the number of unique
#         characters in each group and return the sum of all these numbers.
# Part 2: Similar, but instead of finding the unique characters, find the
#         number of characters that occur in each life of the group.
#


with open("../inputs/day06.txt") as file:
    lines = file.read().splitlines(keepends=False)

def get_groups(lines: list) -> list:
    group = []
    for line in lines:
        if line == "":
            yield group
            group = []
            continue
        group.append(line)
    yield group # last line

print("Part 1: %i" % sum(len(set("".join(g))) for g in get_groups(lines)))
print("Part 2: %i" % sum( # sums up the common chars in *all* groups
        sum(1 for _ # sums up the common chars in g
            in filter(
                # get all elements within the *shortest* line that are in *all others* also
                lambda c: all([c in answers for answers in g]),
                min(g, key=len)))
        for g in get_groups(lines)))