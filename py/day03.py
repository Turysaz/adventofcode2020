
with open("../inputs/day03.txt") as file:
    lines = [l[:-1] for l in file.readlines()] # trim newlines

def get_crashes(dx: int, dy: int) -> int:
    x, trees = 0, 0
    for row in lines[::dy]:
        if(row[x % len(row)] == "#"):
            trees += 1
        x += dx
    return trees

def part1():
    print("Part 1")
    print(get_crashes(3,1))

def part2():
    print("Part 2")
    a1 = get_crashes(1,1)
    a2 = get_crashes(3,1)
    a3 = get_crashes(5,1)
    a4 = get_crashes(7,1)
    a5 = get_crashes(1,2)
    print(a1 * a2 * a3 * a4 * a5)


part1()
part2()
