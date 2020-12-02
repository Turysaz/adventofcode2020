import re

with open("../inputs/day02.txt") as file:
    lines = file.readlines()

pattern = "(?P<n1>\d+)-(?P<n2>\d+) (?P<sym>\w): (?P<pw>\w+)"

def part1():
    print("Part1")
    valid_c = 0

    for l in lines:
        m = re.match(pattern, l)
        min, max, sym, pw = m.group("n1", "n2", "sym", "pw")
        min, max = int(min), int(max)
        if pw.count(sym) < min or pw.count(sym) > max:
            continue

        valid_c += 1

    print("valid password count: {}".format(valid_c))

def part2():
    print("Part 2")
    valid_c = 0
    for l in lines:
        m = re.match(pattern, l)
        i1, i2, sym, pw = m.group("n1", "n2", "sym", "pw")
        i1, i2 = int(i1)-1, int(i2)-1 # adjusting indices
        if (pw[i1] == sym) != (pw[i2] == sym):
            valid_c += 1
            continue

    print("valid password count: {}".format(valid_c))


part1()
part2()

