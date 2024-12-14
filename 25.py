from itertools import batched
f = open("25.in")
in_raw = f.read().splitlines()
games = []
for line1, line2, line3, line4 in batched(in_raw, 4):
    line1 = line1.removeprefix("Button A: X+")
    line1 = line1.replace(", Y+", " ")
    line2 = line2.removeprefix("Button B: X+")
    line2 = line2.replace(", Y+", " ")
    line3 = line3.removeprefix("Prize: X=")
    line3 = line3.replace(", Y=", " ")
    games.append([list(map(int, line1.split())), list(map(int, line2.split())), list(map(int, line3.split()))])
total_cost = 0
for game in games:
    ax = game[0][0]
    ay = game[0][1]
    bx = game[1][0]
    by = game[1][1]
    rx = game[2][0]
    ry = game[2][1]
    count = rx
    a_presses = 0
    b_presses = 0
    while count != 0:
        if count % bx == 0:
            if a_presses * ay + (b_presses+int(count/bx)) * by == ry:
                b_presses += int(count/bx)
                count -= bx * int(count/bx)
                break
        if count % ax == 0:
            if (a_presses+int(count/ax)) * ay + b_presses * by == ry:
                a_presses += int(count/ax)
                count -= ax * int(count/ax)
                break
        count -= bx
        b_presses += 1
        if count < 0:
            break
    if a_presses * ay + b_presses * by == ry and a_presses * ax + b_presses * bx == rx:
        total_cost += a_presses * 3 + b_presses        
print(total_cost)