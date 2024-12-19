# UNSOLVED

from functools import cache

f = open("37sample.in")

towels = []
patterns = []

for line in f.readlines():
    if "," in line:
        towels = line.strip().split(", ")
        continue
    if line != "\n":
        patterns.append(line.strip())

count = 0

@cache
def good_pattern(pattern, top=True):
    global towels
    global count
    if pattern == "":
        return True
    if pattern in towels:
        return True
    found_good_pattern = False
    for towel in towels:
        if towel in pattern:
            # Can only split the first instance to make sure all possibilites are covered
            remaining = pattern.split(towel, 1)
            is_good_pattern = True
            for segment in remaining:
                if not good_pattern(segment, False):
                    is_good_pattern = False
            if is_good_pattern and top:
                count += 1
            if is_good_pattern:
                found_good_pattern = True
    return found_good_pattern

for pattern in patterns:
    good_pattern(pattern)
print(count)