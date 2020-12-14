from math import prod
with open("../inputs/day10.txt") as file:
    jolts = sorted([int(l) for l in file.readlines()])

# a "sequence" is a consecutive row of 'single steps' (1 step vs. 3 steps)
def f(x: int) -> int:
    "Gets the possible paths through a sequence of length x"
    if(x <= 2): return max(x, 1)
    return f(x-3) + f(x-2) + f(x-1)

jolts = [0] + jolts + [jolts[-1] + 3] #prepend 0 and append +3 for device
sequences, current_seq = [], 0 # get all sequences by their lengths
for i in range(len(jolts) - 1):
    if(jolts[i+1] - jolts[i] == 1):
        current_seq += 1
        continue
    if(current_seq > 0): # end of sequence
        sequences.append(current_seq)
        current_seq = 0

print("Part 1: %i" % ((len(jolts)-1 - sum(sequences)) * sum(sequences)))
print("Part 2: %i" % prod(map(f, sequences)))

