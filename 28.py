from PIL import Image
f = open("27.in")
grid = []
xb = 101
yb = 103
for line in f.readlines():
    line = line.removeprefix("p=")
    line = line.replace(" v=", ",")
    grid.append(list(map(int, line.split(","))))

def elapse():
    global grid
    for robot in grid:
        # robot[0] += (robot[2] * 100 + 1) % xb - 1
        # robot[1] += (robot[3] * 100 + 1) % yb - 1
        robot[0] += robot[2]
        robot[1] += robot[3]
        while robot[0] >= xb:
            robot[0] -= xb
        while robot[1] >= yb:
            robot[1] -= yb
        while robot[0] < 0:
            robot[0] += xb
        while robot[1] < 0:
            robot[1] += yb
steps = 0
for i in range(10000):
    # steps += 1
    # positions = set()
    # for bot in grid:
    #     positions.add((bot[0], bot[1]))
    # if len(positions) == len(grid):
    image = Image.new(size=(xb, yb), mode="RGB", color="white")
    pixels = image.load()
    for bot in grid:
        pixels[bot[0],bot[1]] = (0,0,0)    
    image.save("day14/" + str(i) + ".png")
        # break
    elapse()
