### UNSOLVED

f = open("21.in")
stones = list(map(int, f.read().split()))
def blink():
    global stones
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            ms = str(stone)
            new_stones.append(int(ms[0:int(len(ms)/2)]))
            new_stones.append(int(ms[int(len(ms)/2):len(ms)]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
for i in range(75):
    blink()
print(len(stones))