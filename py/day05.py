
with open("../inputs/day05.txt") as file:
    lines = file.read().splitlines(keepends=False)


def get_id(line: str) -> int:
    row, col = 0, 0
    for c in line[:7]:
        row <<= 1
        row += 1 if c == 'B' else 0
    for c in line[7:]:
        col <<= 1
        col += 1 if c == 'R' else 0
    return row * 8 + col

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

