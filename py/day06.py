with open("../inputs/day06.txt") as file:
    lines = file.read().splitlines(keepends=False)

def split_data(lines: list) -> list:
    latest, size = {}, 0
    for line in lines:
        if line == "":
            yield (latest, size)
            latest, size = {}, 0
            continue

        size += 1

        for c in line:
            if c in latest:
                latest[c] += 1
            else:
                latest[c] = 1

    yield (latest, size) # last line

def part1():
    return sum(len(group[0]) for group in split_data(lines))

def part2():
    s = 0
    for group in split_data(lines):
        for ans in group[0]:
            s += int(group[0][ans] == group[1])
    return s

print("Part 1: %i" % part1())
print("Part 2: %i" % part2())

