from math import prod
with open("../inputs/day10.txt") as file:
    adapters = sorted([int(l) for l in file.readlines()])

def solve(jolts):
    def f(x):
        if(x <= 1): return 1
        if(x == 2): return 2
        return f(x-3) + f(x-2) + f(x-1)
    jolts = [0] + jolts + [jolts[-1] + 3] #prepend 0 and append +3 for device
    one_sequences = []
    current = 0
    for i in range(len(jolts) - 1):
        if(jolts[i+1] - jolts[i] == 1):
            current += 1
        elif(jolts[i+1] - jolts[i] == 3):
            if(current > 0):
                one_sequences.append(current)
                current = 0
    print((len(jolts) - 1 - sum(one_sequences)) * sum(one_sequences))
    print(prod(map(f, one_sequences)))

solve(adapters)
