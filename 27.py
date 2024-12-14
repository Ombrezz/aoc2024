f = open("27.in")
grid = []
xb = 101
yb = 103
for line in f.readlines():
    line = line.removeprefix("p=")
    line = line.replace(" v=", ",")
    grid.append(list(map(int, line.split(","))))

tl = 0
tr = 0
bl = 0
br = 0

for robot in grid:
    # robot[0] += (robot[2] * 100 + 1) % xb - 1
    # robot[1] += (robot[3] * 100 + 1) % yb - 1
    robot[0] += robot[2] * 100
    robot[1] += robot[3] * 100
    while robot[0] >= xb:
        robot[0] -= xb
    while robot[1] >= yb:
        robot[1] -= yb
    while robot[0] < 0:
        robot[0] += xb
    while robot[1] < 0:
        robot[1] += yb
    if robot[0] < (xb-1)/2 and robot[1] < (yb-1)/2:
        tl += 1
    if robot[0] > (xb-1)/2 and robot[1] < (yb-1)/2:
        tr += 1
    if robot[0] < (xb-1)/2 and robot[1] > (yb-1)/2:
        bl += 1
    if robot[0] > (xb-1)/2 and robot[1] > (yb-1)/2:
        br += 1
print(tl, tr, bl, br)
print((xb-1)/2, (yb-1)/2)
print(tl * tr * bl * br)