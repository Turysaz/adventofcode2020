with open("../inputs/day15.txt") as file:
    start = [int(x) for x in file.readline().split(",")]

def get_nth_number(n: int) -> int:
    last_time_of = {v:start.index(v)+1 for v in start[:-1]}
    turn = len(start)
    last_spoken = start[-1]

    while turn < n:
        if last_spoken not in last_time_of:
            speak = 0
        else:
            speak = turn - last_time_of[last_spoken]
        last_time_of[last_spoken] = turn
        last_spoken = speak
        turn += 1

    return last_spoken

print("Part 1: %i" % get_nth_number(2020))
print("Part 2: %i" % get_nth_number(30000000))

