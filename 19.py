from collections import defaultdict
f = open("19.in")
map = {}
for y, line in enumerate(f.readlines()):
    for x, tile in enumerate(line):
        if tile != "\n" and tile != ".":
            map[(x,y)] = int(tile)
reaches = defaultdict(set)
def explore_head(x, y, n, og):
    global reaches
    if n == 9:
        reaches[og].add((x,y))
        return
    if (x+1,y) in map:
        if map[(x+1,y)] == n+1:
            explore_head(x+1, y, n+1, og)
    if (x-1,y) in map:
        if map[(x-1,y)] == n+1:
            explore_head(x-1, y, n+1, og)
    if (x,y+1) in map:
        if map[(x,y+1)] == n+1:
            explore_head(x, y+1, n+1, og)
    if (x,y-1) in map:
        if map[(x,y-1)] == n+1:
            explore_head(x, y-1, n+1, og)
for pos in map:
    if map[pos] == 0:
        explore_head(pos[0], pos[1], 0, (pos[0], pos[1]))
sum = 0
for reach in reaches:
    sum += len(reaches[reach])
print(sum)