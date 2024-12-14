from collections import defaultdict
f = open("11.in")
obstacles = []
visited = defaultdict(list)
pos = (0,0)
dir = "up"
for i, line in enumerate(f.readlines()):
    for j, spot in enumerate(line):
        if spot == "#":
            obstacles.append((i,j))
        elif spot == "^":
            pos = (i,j)

def check(obstacles, pos, dir):
    visited.clear()
    while pos[0] < 130 and pos[0] >= 0 and pos[1] < 130 and pos[1] >= 0:
        if dir in visited[pos]:
            return True
        visited[pos].append(dir)
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
    return False

count = 0

for i in range(130):
    for j in range(130):
        new_obs = obstacles.copy()
        new_obs.append((i,j))
        if check(new_obs, pos, "up"):
            count += 1
            print(count)
        if j == 0:
            print("I" + str(i))
print(count)