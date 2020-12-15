import re
with open("../inputs/day14.txt") as file:
    program = file.readlines()


def part1():
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

def part2():
    def possible_masks(mask: str):
        m = [(0,0,0)] # ANDFLOAT, OR, ORFLOAT
        for c in mask:
            for i in range(len(m)):
                m[i] = (m[i][0] << 1, m[i][1] << 1, m[i][2] << 1)
                if c in "10":
                    m[i] = (m[i][0] + 1, m[i][1] + int(c), m[i][2])
                if c == "X":
                    m.append((m[i][0] + 1, m[i][1], m[i][2]+1))
        return m
    def all_addresses(raw, masks):
        addresses = []
        for m in masks:
            addresses.append((raw | m[1]) & m[0] | m[2])
        return addresses
        
    mem = {}
    masks = []
    for l in program:
        mask_pattern = r"mask = (?P<pat>[X10]{36})"
        memo_pattern = r"mem\[(?P<add>\d*)\] = (?P<val>\d*)"
        mmask=re.match(mask_pattern, l)
        mmemo=re.match(memo_pattern, l)
        if mmask != None:
            masks = possible_masks(mmask.group("pat"))
            continue
        if mmemo != None:
            addresses = all_addresses(int(mmemo.group("add")), masks)
            for a in addresses:
                mem[a] = int(mmemo.group("val"))
    print("Part 2: %i" % sum(mem.values()))

part1()
part2()

