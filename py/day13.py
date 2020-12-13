with open("../inputs/day13.txt") as file:
    current_timestamp = int(file.readline())
    bus_lines = [int(line) for line in file.readline().split(",") if line != "x"]

def get_wait_time(timestamp, line):
    return line - (current_timestamp % line)

min_line = min(bus_lines, key=(lambda x: get_wait_time(current_timestamp, x)))
print("Part1: %i" % (min_line * get_wait_time(current_timestamp, min_line)))

