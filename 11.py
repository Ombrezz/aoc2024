f = open("11.in")
obstacles = []
visited = set()
pos = (0,0)
dir = "up"
for i, line in enumerate(f.readlines()):
    for j, spot in enumerate(line):
        if spot == "#":
            obstacles.append((i,j))
        elif spot == "^":
            pos = (i,j)
while pos[0] < 130 and pos[0] >= 0 and pos[1] < 130 and pos[1] >= 0:
    visited.add(pos)
    if dir == "up":
        next = (pos[0]-1,pos[1])
        if next in obstacles:
            dir = "right"
        else:
            pos = next
    if dir == "right":
        next = (pos[0],pos[1]+1)
        if next in obstacles:
            dir = "down"
        else:
            pos = next
    if dir == "down":
        next = (pos[0]+1,pos[1])
        if next in obstacles:
            dir = "left"
        else:
            pos = next
    if dir == "left":
        next = (pos[0],pos[1]-1)
        if next in obstacles:
            dir = "up"
        else:
            pos = next
print(len(visited))