# TODO: Make blink only operate on one stone at a time so cache can actually do its job
from functools import cache
f = open("21.in")
stones = list(map(int, f.read().split()))
@cache
def blink(stone):
    new_stones = []
    if stone == 0:
        new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
        ms = str(stone)
        new_stones.append(int(ms[0:int(len(ms)/2)]))
        new_stones.append(int(ms[int(len(ms)/2):len(ms)]))
    else:
        new_stones.append(stone * 2024)
    return new_stones
for i in range(75):
    print(i)
    new_stones = []
    for stone in stones:
        new_stones.extend(blink(stone))
    stones = new_stones
print(len(stones))