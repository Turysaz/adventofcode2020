with open("../inputs/day13.txt") as file:
    current_timestamp = int(file.readline())
    bus_lines = [int(line) for line in file.readline().split(",") if line != "x"]

_min = 99999999
_min_line = None
for l in bus_lines:
    n = l - (current_timestamp % l)
    if n < _min:
        _min = n
        _min_line = l

print(_min)
print(_min_line )
print(_min_line * _min)

