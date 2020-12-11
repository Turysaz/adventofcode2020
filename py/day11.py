with open("../inputs/day11.txt") as file:
    seat_map = file.read().splitlines(keepends=False)

def get_seat(grid, x, y):
    if -1 >= x or x >= len(grid[0]): return "x" # "x" marks out of range
    if -1 >= y or y >= len(grid): return "x"
    return grid[y][x]

# mapping
def new_state(grid, x, y, tolerance, recurse):
    """
    Gets the new value of a grid cell considering the tolerance of other people
    before leaving the seat.
    The "recurse" option switches between direct neighbors and first seat in
    line of sight.
    """
    def relative_taken(base, offset, recurse):
        n_x, n_y = base[0] + offset[0], base[1] + offset[1]
        n_state = get_seat(grid, n_x, n_y)
        if n_state == "x":
            return False
        if n_state == ".":
            return False if not recurse else relative_taken((n_x, n_y), offset, recurse)
        return n_state == "#"
    
    if get_seat(grid, x, y) == ".":
        return "."

    directions = [(x,y) for x in [-1,0,1] for y in [-1,0,1] if x != 0 or y != 0]
    taken_l = [relative_taken((x, y), d, recurse) for d in directions]
    taken = taken_l.count(True)
    if taken == 0: return "#"
    if taken > tolerance: return "L"
    return get_seat(grid,x,y)

def run_to_stable(g, tolerance, recurse):
    changed = True
    while changed:
        changed = False
        newgrid = []
        for y in range(len(g)):
            newline = ""
            for x in range(len(g[0])):
                old = get_seat(g, x, y)
                new = new_state(g, x, y, tolerance, recurse)
                if(new != old):
                    changed = True
                newline += new
            newgrid.append(newline)
        g = newgrid

    return sum([l.count("#") for l in g])

print("Part 1: %i" % run_to_stable(seat_map, 3, False))
print("Part 2: %i" % run_to_stable(seat_map, 4, True))
