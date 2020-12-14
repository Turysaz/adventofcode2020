from itertools import combinations
with open("../inputs/day09.txt") as file:
    numbers = [int(line) for line in file.readlines()]

def find_weak(numbers, rot=25):
    target = 0
    buffer = numbers[:rot]
    for j in range(len(numbers) - rot):
        i = j + rot
        target = numbers[i]
        if not any(map(
                lambda x : (x[0] != x[1] and sum(x) == target),
                combinations(buffer, 2))):
            return target
        buffer[i%rot] = target

def find_seq(numbers, weak):
    chunklen = 2
    while(chunklen < len(numbers)):
        for j in range(len(numbers) - chunklen):
            buffer = numbers[j:chunklen+j]
            if(sum(buffer) == weak):
                return buffer
        chunklen += 1

def crackXMAS(numbers, rot=25):
    weak = find_weak(numbers, rot)
    print("Part 1: {}".format(weak))
    seq = find_seq(numbers, weak)
    _min, _max = min(seq), max(seq)
    print("Part 2: {}".format(_min+_max))

crackXMAS(numbers, 25)
