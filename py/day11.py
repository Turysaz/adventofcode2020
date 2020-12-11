from itertools import combinations
with open("../inputs/day11.txt") as file:
    grid = file.read().splitlines(keepends=False)

grid_d = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##""".splitlines(keepends=False)

def get_seat(g,x,y): #get state char
    if -1 >= x or x >= len(g[0]): return "e"
    if -1 >= y or y >= len(g): return "e"
    return g[y][x]

# mapping
def new_state(g,x,y,tolerance,recurse):
    def neighbor_taken(base, vec, recurse):
        _x, _y = base[0] + vec[0], base[1] + vec[1]
        v = get_seat(g, _x, _y)
        if v == "e":
            return -1
        if v == ".":
            return -1 if not recurse else neighbor_taken((_x, _y), vec, recurse)
        return 1 if v == "#" else -1
    
    if get_seat(g, x, y) == ".":
        return "."
    directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
    new = sum([neighbor_taken((x, y), d, recurse) for d in directions])

    if new == -8: return "#"
    if new >= tolerance - 4: return "L"
    return get_seat(g,x,y)

def run_to_stable(g, tolerance, recurse):
    changed = True
    rounds = 0
    while changed:
        rounds += 1
        changed = False
        newgrid = []
        for y in range(len(g)):
            newline = ""
            for x in range(len(g[0])):
                old = get_seat(g,x,y)
                new = new_state(g,x,y, tolerance, recurse)
                if(new != old):
                    changed = True
                newline += new
            newgrid.append(newline)
        g = newgrid

    print("stable after %i rounds:" % rounds)
    occupied = 0
    for l in g:
        occupied += l.count("#")
        #print(l)
    print("TakenSeats: %i" % occupied)

# 1: 37  2166
# 2: 26

run_to_stable(grid_d,4,False)
run_to_stable(grid_d,5,True)
run_to_stable(grid,4,False)
run_to_stable(grid,5,True)
