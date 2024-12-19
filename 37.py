from functools import cache

f = open("37.in")

towels = []
patterns = []

for line in f.readlines():
    if "," in line:
        towels = line.strip().split(", ")
        continue
    if line != "\n":
        patterns.append(line.strip())

@cache
def good_pattern(pattern):
    global towels
    if pattern == "":
        return True
    if pattern in towels:
        return True
    for towel in towels:
        if towel in pattern:
            # Can only split the first instance to make sure all possibilites are covered
            remaining = pattern.split(towel, 1)
            is_good_pattern = True
            for segment in remaining:
                if not good_pattern(segment):
                    is_good_pattern = False
            if is_good_pattern:
                return True
    return False
            
count = 0

for pattern in patterns:
    if good_pattern(pattern):
        count += 1
print(count)