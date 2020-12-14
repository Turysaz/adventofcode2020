import re
with open("../inputs/day14.txt") as file:
    program = file.readlines()

def apply_mask(value: int, mask: str) -> int:
    AND, OR = 0, 0
    for c in mask:
        AND <<= 1
        OR <<= 1
        if c == "X":
            OR += 0
            AND += 1
        else:
            OR += int(c)
            AND += int(c)
    return ((value | OR) & AND)

mem = {}
mask = "X" * 36

for l in program:
    mask_pattern = r"mask = (?P<pat>[X10]{36})"
    memo_pattern = r"mem\[(?P<add>\d*)\] = (?P<val>\d*)"
    mmask=re.match(mask_pattern, l)
    mmemo=re.match(memo_pattern, l)
    if mmask != None:
        mask = mmask.group("pat")
        continue
    if mmemo != None:
        mem[int(mmemo.group("add"))] = apply_mask(int(mmemo.group("val")), mask)

print("Part 1: %i" % sum(mem.values()))
