
with open("../inputs/day05.txt") as file:
    lines = file.read().splitlines(keepends=False)

def get_id(line: str) -> int:
    x = 0
    for c in line:
        x = (x << 1) | int(c in "RB")
    return x

ids = [get_id(line) for line in lines]
ids.sort()

print("Part 1: %i" % ids[-1])

for i in range(len(ids) - 2): # -1 because of start index 0, -1 for lookahead
    if ids[i] + 2 == ids[i+1]: # + 2 to find gap
        print("Part 2: %i" % (ids[i] + 1)) # get gap
        exit()
