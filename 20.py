from collections import defaultdict
f = open("19.in")
map = {}
for y, line in enumerate(f.readlines()):
    for x, tile in enumerate(line):
        if tile != "\n" and tile != ".":
            map[(x,y)] = int(tile)
sum = 0
def explore_head(x, y, n):
    global sum
    if n == 9:
        sum += 1
        return
    if (x+1,y) in map:
        if map[(x+1,y)] == n+1:
            explore_head(x+1, y, n+1)
    if (x-1,y) in map:
        if map[(x-1,y)] == n+1:
            explore_head(x-1, y, n+1)
    if (x,y+1) in map:
        if map[(x,y+1)] == n+1:
            explore_head(x, y+1, n+1)
    if (x,y-1) in map:
        if map[(x,y-1)] == n+1:
            explore_head(x, y-1, n+1)
for pos in map:
    if map[pos] == 0:
        explore_head(pos[0], pos[1], 0)
print(sum)