with open("../inputs/day12.txt") as file:
    lines = file.read().splitlines(keepends=False)

def solve(useWaypoint):
    pos = 0+0j
    hwp = 10+1j if useWaypoint else 1+0j # heading or way point

    def translate(x):
        nonlocal pos, hwp
        if useWaypoint:
            hwp += x
        else:
            pos += x

    for l in lines:
        ins = l[0]
        arg = int(l[1:])
        if ins == "N": translate(arg * +1j)
        elif ins == "S": translate(arg * -1j)
        elif ins == "E": translate(arg * 1)
        elif ins == "W": translate(arg * -1)
        elif ins == "F": pos += hwp * arg
        elif ins == "R": hwp *= (-1j) ** int(arg/90)
        elif ins == "L": hwp *= (+1j) ** int(arg/90)

    return(abs(pos.real) + abs(pos.imag))

print("Part 1: %i" % solve(useWaypoint=True))
print("Part 2: %i" % solve(useWaypoint=False))
