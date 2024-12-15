from time import sleep

f = open("29.in")
walls = []
boxes = []
movements = []
bot_pos = (0,0)
for y, line in enumerate(f.readlines()):
    for x, char in enumerate(line):
        if char == "#":
            walls.append((x,y))
        elif char == "O":
            boxes.append((x,y))
        elif char == "@":
            bot_pos = (x,y)
        elif char == "\n" or char == ".":
            continue
        else:
            movements.append(char)

def do_push(x, y, movement=None):
    global walls, boxes, movements, bot_pos
    if movement == None:
        movement = movements.pop(0)
    if movement == "<":
        if (x-1, y) in walls:
            return False
        if (x-1, y) in boxes:
            if do_push(x-1, y, movement):
                boxes[boxes.index((x-1, y))] = (x-2, y)
                return True
            else:
                return False
        return True
    if movement == "^":
        if (x, y-1) in walls:
            return False
        if (x, y-1) in boxes:
            if do_push(x, y-1, movement):
                boxes[boxes.index((x, y-1))] = (x, y-2)
                return True
            else:
                return False
        return True
    if movement == ">":
        if (x+1, y) in walls:
            return False
        if (x+1, y) in boxes:
            if do_push(x+1, y, movement):
                boxes[boxes.index((x+1, y))] = (x+2, y)
                return True
            else:
                return False
        return True
    if movement == "v":
        if (x, y+1) in walls:
            return False
        if (x, y+1) in boxes:
            if do_push(x, y+1, movement):
                boxes[boxes.index((x, y+1))] = (x, y+2)
                return True
            else:
                return False
        return True

for i in range(len(movements)):
    movement = movements[0]
    # print(movement)
    # for y in range(8):
    #     for x in range(8):
    #         if (x, y) in walls:
    #             print("#", end="")
    #         elif (x, y) in boxes:
    #             print("O", end="")
    #         elif bot_pos == (x, y):
    #             print("@", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # sleep(1)
    if movement == "<":
        if do_push(bot_pos[0], bot_pos[1]):
            bot_pos = (bot_pos[0]-1, bot_pos[1])
    if movement == "^":
        if do_push(bot_pos[0], bot_pos[1]):
            bot_pos = (bot_pos[0], bot_pos[1]-1)
    if movement == ">":
        if do_push(bot_pos[0], bot_pos[1]):
            bot_pos = (bot_pos[0]+1, bot_pos[1])
    if movement == "v":
        if do_push(bot_pos[0], bot_pos[1]):
            bot_pos = (bot_pos[0], bot_pos[1]+1)
total = 0
for box in boxes:
    total += box[0] + box[1] * 100
print(total)