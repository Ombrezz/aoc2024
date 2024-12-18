# UNSOLVED

from astar import AStar

class Maze(AStar):
    dir = ""
    maze = []
    def __init__(self, maze):
        super().__init__()
        dir = "east"
        self.maze = maze
    def neighbors(self, node):
        ret = []
        if (node[0]+1, node[1]) not in self.maze:
            ret.append((node[0]+1, node[1]))
        if (node[0]-1, node[1]) not in self.maze:
            ret.append((node[0]-1, node[1]))
        if (node[0], node[1]+1) not in self.maze:
            ret.append((node[0], node[1]+1))
        if (node[0], node[1]-1) not in self.maze:
            ret.append((node[0], node[1]-1))

f = open("31sample.in")
walls = []
start = (0,0)
end = (0,0)
for (y, line) in enumerate(f.readlines()):
    for (x, pos) in enumerate(line):
        if pos == "#":
            walls.append((x, y))
        if pos == "S":
            start = (x, y)
        if pos == "E":
            end = (x, y)
print(walls)