with open("../inputs/day12.txt") as file:
    lines = file.read().splitlines(keepends=False)

def part1():
    pos = 0+0j
    hed = 1+0j

    for l in lines:
        ins = l[0]
        arg = int(l[1:])
        if ins == "N": pos += arg * +1j
        elif ins == "S": pos += arg * -1j
        elif ins == "E": pos += arg * 1
        elif ins == "W": pos += arg * -1
        elif ins == "F": pos += hed * arg
        elif ins == "R":
            for i in range(int(arg/90)):
                hed *= -1j
        elif ins == "L":
            for i in range(int(arg/90)):
                hed *= 1j

    return(abs(pos.real) + abs(pos.imag))

def part2():
    pos = 0+0j
    wp = 10+1j 
    for l in lines:
        ins = l[0]
        arg = int(l[1:])
        if ins == "N": wp += arg * +1j
        elif ins == "S": wp += arg * -1j
        elif ins == "E": wp += arg * 1
        elif ins == "W": wp += arg * -1
        elif ins == "F": pos += wp * arg
        elif ins == "R":
            for i in range(int(arg/90)):
                wp *= -1j
        elif ins == "L":
            for i in range(int(arg/90)):
                wp *= 1j

    return(abs(pos.real) + abs(pos.imag))

print("Part 1: %i" % part1())
print("Part 2: %i" % part2())
