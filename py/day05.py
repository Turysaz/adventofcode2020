
with open("../inputs/day05.txt") as file:
    lines = file.read().splitlines(keepends=False)


def get_id(line: str) -> int:
    x = 0
    for c in line:
        x <<= 1
        x += 1 if c in "RB" else 0
    return x

ids = [get_id(line) for line in lines]
_max = max(ids)

print("Part 1")
print(_max)

print("Part 2")

ids.sort()
for i in range(len(ids) - 2): # -1 because of start index 0, -1 for lookahead
    if ids[i] + 2 == ids[i+1]: # + 2 to find gap
        print(ids[i] + 1) # get gap
        exit()

