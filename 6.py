import re

regex = "mul\(\d+,\d+\)"

f = open("5.in")

txt = f.read()
txt.split

matches = re.finditer(regex, txt)
dos = re.finditer("do\(\)", txt)
donts = re.finditer("don't\(\)", txt)

sum = 0

store = {}

for match in matches:
    store[match.start()] = match.group()
    #match = match.removeprefix("mul(")
    #match = match.removesuffix(")")
    #match = list(map(int, match.split(",")))
    #sum += match[0] * match[1]
for do in dos:
    store[do.start()] = do.group()
for dont in donts:
    store[dont.start()] = dont.group()

store = dict(sorted(store.items()))
do = True
for command in store.values():
    if command == "do()":
        do = True
    elif command == "don't()":
        do = False
    elif do:
        command = command.removeprefix("mul(")
        command = command.removesuffix(")")
        command = list(map(int, command.split(",")))
        sum += command[0] * command[1]
        print(command[0], command[1])
print(sum)