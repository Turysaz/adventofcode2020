
with open("../inputs/day06.txt") as file:
    lines = file.read().splitlines(keepends=False)

def split_data(lines: list) -> list:
    latest = ""
    for line in lines:
        latest += line
        if(line == ""):
            yield latest
            latest = "" # reset
    yield latest # last line

def part1():
    return sum(len(set(ans for ans in group)) for group in split_data(lines))

print("Part 1: %i" % part1())

