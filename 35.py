from astar import AStar
from math import hypot
f = open("35.in")
coords = []
for line in f.readlines():
    coords.append(tuple(map(int, line.split(","))))
walls = coords[:1024]

class Solver(AStar):
    walls = []
    bounds = 0
    def __init__(self, walls, bounds):
        super().__init__()
        self.walls = walls
        self.bounds = bounds

    def astar(self, start, reversePath = False):
        return super().astar(start, (self.bounds, self.bounds), reversePath)

    def neighbors(self, node):
        ret = []
        if (node[0] + 1, node[1]) not in self.walls and node[0] + 1 <= self.bounds:
            ret.append((node[0] + 1, node[1]))
        if (node[0] - 1, node[1]) not in self.walls and node[0] - 1 >= 0:
            ret.append((node[0] - 1, node[1]))
        if (node[0], node[1] + 1) not in self.walls and node[1] + 1 <= self.bounds:
            ret.append((node[0], node[1] + 1))
        if (node[0], node[1] - 1) not in self.walls and node[1] - 1 >= 0:
            ret.append((node[0], node[1] - 1))
        
        return ret
    
    def distance_between(self, n1, n2):
        return 1
    
    def heuristic_cost_estimate(self, current, goal):
        return hypot(goal[0] - current[0], goal[1] - current[1])

solver = Solver(walls, 70)

path = list(solver.astar((0,0)))

print(path)

for y in range(71):
    for x in range(71):
        if (x, y) in walls:
            print("#", end="")
        elif (x, y) in path:
            print("O", end="")
        else:
            print(".", end="")
    print()
print(len(path)-1)