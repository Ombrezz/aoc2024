f = open("33.in")
a = 0
b = 0
c = 0
prog = []
for line in f.readlines():
    if "A" in line:
        a = int(line.removeprefix("Register A: "))
    if "B" in line:
        b = int(line.removeprefix("Register B: "))
    if "C" in line:
        c = int(line.removeprefix("Register C: "))
    if "P" in line:
        prog = list(map(int, line.removeprefix("Program: ").split(",")))
def run_prog(a, b, c, prog):
    output = []
    pointer = 0
    while pointer < len(prog):
        inst = prog[pointer]
        combo = prog[pointer+1]
        literal = prog[pointer+1]
        if combo == 4:
            combo = a
        elif combo == 5:
            combo = b
        elif combo == 6:
            combo = c
        if inst == 0:
            a = int(a / 2**combo)
            pointer += 2
            continue
        if inst == 1:
            b = b ^ literal
            pointer += 2
            continue
        if inst == 2:
            b = combo % 8
            pointer += 2
            continue
        if inst == 3:
            if a != 0:
                pointer = literal
                continue
            pointer += 2
            continue
        if inst == 4:
            b = b ^ c
            pointer += 2
            continue
        if inst == 5:
            output.append(combo % 8)
            pointer += 2
            continue
        if inst == 6:
            b = int(a / 2**combo)
            pointer += 2
            continue
        if inst == 7:
            c = int(a / 2**combo)
            pointer += 2
            continue
    return output
a = 0
while True:
    if a % 10000 == 0:
        print(a)
    if prog == run_prog(a, b, c, prog):
        print(a)
        break
    a += 1