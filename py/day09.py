
from itertools import combinations
with open("../inputs/day09.txt") as file:
    numbers = [int(line) for line in file.readlines()]

def crackXMAS(numbers, rot=25):
    target = 0
    buffer = numbers[:rot]
    for j in range(len(numbers) - rot):
        i = j + rot
        target = numbers[i]
        if not any(map(
                lambda x : (x[0] != x[1] and sum(x) == target),
                combinations(buffer, 2))):
            print("weakness: %i" % target)
            break
        buffer[i%rot] = target
    chunklen = 2
    while(chunklen < len(numbers)):
        for j in range(len(numbers) - chunklen):
            buffer = numbers[j:chunklen+j]
            if(sum(buffer) == target):
                _min, _max = min(buffer), max(buffer)
                print("Seq: {}, Min: {}, Max:{}, Sum:{}".format(buffer, _min, _max, _min+_max))
                return
        chunklen += 1

crackXMAS(numbers, 25)
