with open("../inputs/day08.txt") as file:
    lines = file.readlines()

def vm(lines):
    visited = set()
    ip, acc = 0, 0
    while(ip not in visited):
        if ip == len(lines):
            return (True, acc)
        visited.add(ip)
        ins, arg = lines[ip].split()
        if ins == "jmp":
            ip += int(arg)
            continue
        if ins == "acc":
            acc += int(arg)
        ip += 1
    return (False, acc)

def flip(ins):
    if "nop" in ins: return ins.replace("nop", "jmp")
    if "jmp" in ins: return ins.replace("jmp", "nop")
    return ins

print("Part 1: %i" % vm(lines)[1])

for i in range(len(lines)):
    lines[i] = flip(lines[i])
    if vm(lines)[0]:
        print("Part 2: %i" % vm(lines)[1])
        break
    lines[i] = flip(lines[i])
