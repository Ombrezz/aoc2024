from collections import defaultdict
f = open("23.in")
grid = defaultdict(list)
bounds = 0
for y, line in enumerate(f.readlines()):
    for x, cell in enumerate(line):
        if cell != "\n":
            grid[cell].append((x,y))
    bounds = y+1
regions = defaultdict(list)
def explore(t, x, y, f):
    global grid
    contig = [(x,y)]
    f.append((x,y))
    if (x+1, y) in grid[t] and (x+1, y) not in f:
        contig.extend(explore(t, x+1, y, f))
    if (x-1, y) in grid[t] and (x-1, y) not in f:
        contig.extend(explore(t, x-1, y, f))
    if (x, y+1) in grid[t] and (x, y+1) not in f:
        contig.extend(explore(t, x, y+1, f))
    if (x, y-1) in grid[t] and (x, y-1) not in f:
        contig.extend(explore(t, x, y-1, f))
    return contig

for t in grid:
    found = []
    while len(found) != len(grid[t]):
        found = []
        for f in regions[t]:
            found.extend(f)
        for pos in grid[t]:
            if pos not in found:
                regions[t].append(explore(t, pos[0], pos[1], [pos]))
                break


total = 0
for t in regions:
    for region in regions[t]:
        sides = 0
        tops = []
        bottoms = []
        for cell in region:
            if (cell[0], cell[1]+1) not in region:
                tops.append(cell)
            if (cell[0], cell[1]-1) not in region:
                bottoms.append(cell)
        for top in tops:
            if (top[0]+1,top[1]) not in tops:
                sides += 1
        for bottom in bottoms:
            if (bottom[0]+1,bottom[1]) not in bottoms:
                sides += 1        
        sides *= 2
        total += sides * len(region)
print(total)