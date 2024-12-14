from collections import defaultdict

sum = 0

puzzle_raw = []
puzzle = defaultdict(lambda: "")

f = open("7.in")

for line in f.readlines():
    puzzle_raw.append(list(line))

for x in range(len(puzzle_raw)):
    for y in range(len(puzzle_raw[x])):
        puzzle[(x, y)] = puzzle_raw[x][y]
for x in range(len(puzzle_raw)):
    for y in range(len(puzzle_raw[x])):
        if puzzle[(x,y)] == "X":
            if puzzle[(x+1,y)] == "M":
                if puzzle[(x+2,y)] == "A":
                    if puzzle[(x+3,y)] == "S":
                        sum += 1
            if puzzle[(x-1,y)] == "M":
                if puzzle[(x-2,y)] == "A":
                    if puzzle[(x-3,y)] == "S":
                        sum += 1
            if puzzle[(x,y+1)] == "M":
                if puzzle[(x,y+2)] == "A":
                    if puzzle[(x,y+3)] == "S":
                        sum += 1
            if puzzle[(x,y-1)] == "M":
                if puzzle[(x,y-2)] == "A":
                    if puzzle[(x,y-3)] == "S":
                        sum += 1
            if puzzle[(x+1,y+1)] == "M":
                if puzzle[(x+2,y+2)] == "A":
                    if puzzle[(x+3,y+3)] == "S":
                        sum += 1
            if puzzle[(x-1,y-1)] == "M":
                if puzzle[(x-2,y-2)] == "A":
                    if puzzle[(x-3,y-3)] == "S":
                        sum += 1
            if puzzle[(x+1,y-1)] == "M":
                if puzzle[(x+2,y-2)] == "A":
                    if puzzle[(x+3,y-3)] == "S":
                        sum += 1
            if puzzle[(x-1,y+1)] == "M":
                if puzzle[(x-2,y+2)] == "A":
                    if puzzle[(x-3,y+3)] == "S":
                        sum += 1
print(sum)
            