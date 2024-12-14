from collections import defaultdict
f = open("23.in")
grid = defaultdict(list)
for y, line in enumerate(f.readlines()):
    for x, cell in enumerate(line):
        if cell != "\n":
            grid[cell].append((x,y))
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
        perimeter = 0
        for cell in region:
            x = cell[0]
            y = cell[1]
            if (x+1,y) in region and (x-1,y) in region and (x,y+1) in region and (x,y-1) in region:
                continue
            elif (x+1,y) in region and (x-1,y) in region and (x,y+1) in region:
                perimeter += 1
            elif (x-1,y) in region and (x,y+1) in region and (x,y-1) in region:
                perimeter += 1
            elif (x+1,y) in region and (x-1,y) in region and (x,y-1) in region:
                perimeter += 1
            elif (x,y+1) in region and (x,y-1) in region and (x+1,y) in region:
                perimeter += 1
            elif (x+1,y) in region and (x-1,y) in region:
                perimeter += 2
            elif (x,y+1) in region and (x,y-1) in region:
                perimeter += 2
            elif (x,y+1) in region and (x+1,y) in region:
                perimeter += 2
            elif (x,y+1) in region and (x-1,y) in region:
                perimeter += 2
            elif (x,y-1) in region and (x+1,y) in region:
                perimeter += 2
            elif (x,y-1) in region and (x-1,y) in region:
                perimeter += 2
            elif (x,y-1) in region:
                perimeter += 3
            elif (x,y+1) in region:
                perimeter += 3
            elif (x-1,y) in region:
                perimeter += 3
            elif (x+1,y) in region:
                perimeter += 3
            else:
                perimeter += 4
        total += perimeter * len(region)
print(total)
