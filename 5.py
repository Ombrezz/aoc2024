import re

regex = "mul\(\d+,\d+\)"

f = open("5.in")

matches = re.findall(regex, f.read())

sum = 0

for match in matches:
    match = match.removeprefix("mul(")
    match = match.removesuffix(")")
    match = list(map(int, match.split(",")))
    sum += match[0] * match[1]
print(sum)