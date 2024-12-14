from collections import defaultdict, Counter
from itertools import combinations
f = open("15.in")

grid = defaultdict(list)
bounds = 0

for y, line in enumerate(f.readlines()):
    bounds = len(line)
    for x, cell in enumerate(line):
        if cell != "." and cell != "\n":
            grid[cell].append((x,y))
antinodes = set()
print(bounds)
for freq in grid:
    print(freq)
    position_pairs = list(combinations(grid[freq], 2))
    for position_pair in position_pairs:
        transform_x_1 = position_pair[0][0] - position_pair[1][0]
        transform_y_1 = position_pair[0][1] - position_pair[1][1]
        transform_x_2 = -transform_x_1
        transform_y_2 = -transform_y_1
        for i in range(bounds):
            final_x_1 = position_pair[0][0] + transform_x_1 * i
            final_y_1 = position_pair[0][1] + transform_y_1 * i
            final_x_2 = position_pair[1][0] + transform_x_2 * i
            final_y_2 = position_pair[1][1] + transform_y_2 * i
            if final_x_1 < bounds and final_x_1 >= 0 and final_y_1 < bounds and final_y_1 >= 0:
                antinodes.add((final_x_1, final_y_1))
            if final_x_2 < bounds and final_x_2 >= 0 and final_y_2 < bounds and final_y_2 >= 0:
                antinodes.add((final_x_2, final_y_2))
print(len(antinodes))
print(antinodes)
map = ""
for y in range(bounds):
    for x in range(bounds):
        if (x, y) in antinodes:
            map += "#"
        else:
            map += "."
    map += "\n"
print(map)
print(Counter(map)["#"])
print(bounds)