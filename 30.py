# UNSOLVED

from time import sleep

f = open("29sample.in")
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

for i in range(len(walls)):
    walls.append((walls[i][0]*2 + 1, walls[i][1]))
    walls[i] = (walls[i][0]*2, walls[i][1])

for i in range(len(boxes)):
    boxes[i] = (boxes[i][0] * 2, boxes[i][1])

bot_pos = (bot_pos[0] * 2, bot_pos[1])

push_stack = []

def do_push(x, y, movement=None, box=False):
    global walls, boxes, movements, bot_pos, push_stack
    if movement == None:
        movement = movements.pop(0)
    if movement == "<":
        if (x-2, y) in walls:
            return False
        if (x-2, y) in boxes:
            if do_push(x-2, y, movement, True):
                boxes[boxes.index((x-2, y))] = (x-3, y)
                return True
            else:
                return False
        else:
            return True
    if movement == "^":
        if not box:
            if (x, y-1) in walls:
                return False
            if (x, y-1) in boxes:
                if do_push(x, y-1, movement, True):
                    boxes[boxes.index((x, y-1))] = (x, y-2)
                    return True
                else:
                    return False
            if (x-1, y-1) in boxes:
                if do_push(x-1, y-1, movement, True):
                    boxes[boxes.index((x-1, y-1))] = (x-1, y-2)
                    return True
                else:
                    return False
            return True
        else:
            if (x, y-1) in walls or (x+1, y-1) in walls:
                for item in push_stack:
                    boxes[boxes.index(item)] = (item[0], item[1] + 1)
                return False
            if (x, y-1) in boxes:
                if do_push(x, y-1, movement, True):
                    boxes[boxes.index((x, y-1))] = (x, y-2)
                    push_stack.append((x, y-2))
                    return True
                else:
                    return False
            pushed_left = None
            pushed_right = None
            if (x-1, y-1) in boxes:
                pushed_left = do_push(x, y-1, movement, True)
            if (x+1, y-1) in boxes:
                pushed_right = do_push(x+1, y-1, movement, True)
            if pushed_left and pushed_right:
                boxes[boxes.index((x-1, y-1))] = (x-1, y-2)
                push_stack.append((x-1, y-2))
                boxes[boxes.index((x+1, y-1))] = (x+1, y-2)
                push_stack.append((x-1, y-2))
                return True
            elif pushed_left == None and pushed_right == None:
                return True
            else:
                return False
    if movement == ">":
        if not box:
            if (x+1, y) in walls:
                return False
            if (x+1, y) in boxes:
                if do_push(x+1, y, movement, True):
                    boxes[boxes.index((x+1, y))] = (x+2, y)
                    return True
                else:
                    return False
            else:
                return True
        else:
            if (x+2, y) in walls:
                return False
            if (x+2, y) in boxes:
                if do_push(x+2, y, movement, True):
                    boxes[boxes.index((x+2, y))] = (x+3, y)
                    return True
                else:
                    return False
            else:
                return True
    if movement == "v":
        if not box:
            if (x, y+1) in walls:
                return False
            if (x, y+1) in boxes:
                if do_push(x, y+1, movement, True):
                    boxes[boxes.index((x, y+1))] = (x, y+2)
                    return True
                else:
                    return False
            if (x-1, y+1) in boxes:
                if do_push(x-1, y+1, movement, True):
                    boxes[boxes.index((x-1, y+1))] = (x-1, y+2)
                    return True
                else:
                    return False
            return True
        else:
            if (x, y+1) in walls or (x+1, y+1) in walls:
                for item in push_stack:
                    boxes[boxes.index(item)] = (item[0], item[1] - 1)
                return False
            if (x, y+1) in boxes:
                if do_push(x, y+1, movement, True):
                    boxes[boxes.index((x, y+1))] = (x, y+2)
                    push_stack.append((x, y+2))
                    return True
                else:
                    return False
            pushed_left = None
            pushed_right = None
            if (x-1, y+1) in boxes:
                pushed_left = do_push(x, y+1, movement, True)
            if (x+1, y+1) in boxes:
                pushed_right = do_push(x+1, y+1, movement, True)
            if pushed_left and pushed_right:
                boxes[boxes.index((x-1, y+1))] = (x-1, y+2)
                push_stack.append((x-1, y+2))
                boxes[boxes.index((x+1, y+1))] = (x+1, y+2)
                push_stack.append((x-1, y+2))
                return True
            elif pushed_left == None and pushed_right == None:
                return True
            else:
                return False
for i in range(len(movements)):
    movement = movements[0]
    # print(movement, bot_pos)
    # for y in range(10):
    #     for x in range(20):
    #         if (x, y) in walls:
    #             print("#", end="")
    #         elif (x, y) in boxes:
    #             print("[]", end="")
    #         elif bot_pos == (x, y):
    #             print("@", end="")
    #         elif (x-1, y) not in boxes:
    #             print(".", end="")
    #     print()
    # sleep(0.1)
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
    push_stack.clear()
total = 0
for box in boxes:
    total += box[0] + box[1] * 100
print(total)
for y in range(10):
    for x in range(20):
        if (x, y) in walls:
            print("#", end="")
        elif (x, y) in boxes:
            print("[]", end="")
        elif bot_pos == (x, y):
            print("@", end="")
        elif (x-1, y) not in boxes:
            print(".", end="")
    print()