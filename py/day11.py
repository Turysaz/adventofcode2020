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

def gsc(g,x,y): #get state char
    if -1 >= x or x >= len(g[0]): return "."
    if -1 >= y or y >= len(g): return "."
    return g[y][x]

# mapping
def new_state(g,x,y):
    def gs(x,y):
        m={"L" : -1, "." : -1, "#" : +1}
        return m[gsc(g,x,y)]

    if gsc(g,x,y) == ".":
        return "."
    new = (
        gs(x-1,y-1) + gs(x+0,y-1) + gs(x+1,y-1) +
        gs(x-1,y+0) +           0 + gs(x+1,y+0) +
        gs(x-1,y+1) + gs(x+0,y+1) + gs(x+1,y+1))

    if new == -8: return "#"
    if new >= 0: return "L"
    return gsc(g,x,y)

def run_to_stable(g):
    changed = True
    rounds = 0
    while changed:
        rounds += 1
        changed = False
        newgrid = []
        for y in range(len(g)):
            newline = ""
            for x in range(len(g[0])):
                old = gsc(g,x,y)
                new = new_state(g,x,y)
                if(new != old):
                    changed = True
                newline += new
            newgrid.append(newline)
        g = newgrid

    print("stable after %i rounds:" % rounds)
    occupied = 0
    for l in g:
        occupied += l.count("#")
        print(l)
    print("TakenSeats: %i" % occupied)

run_to_stable(grid)
