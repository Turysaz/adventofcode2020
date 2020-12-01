
with open("../inputs/day01.txt") as file:
    entries = [int(line) for line in file.readlines()]


def part1():
    print("part 1")
    for s1 in entries:
        for s2 in entries:
            if s1 + s2 == 2020:
                print("{}, {}".format(s1, s2))
                print(s1 * s2)
                return

def part2():
    print("part 2")
    for s1 in entries:
        for s2 in entries:
            for s3 in entries:
                if s1 + s2 + s3 == 2020:
                    print("{}, {}, {}".format(s1, s2, s3))
                    print(s1 * s2 * s3)
                    return

part1()
part2()

