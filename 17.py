f = open("17.in")
inp = f.read().strip()
filesystem = []
in_count = 0
for i in range(0,len(inp),2):
    filesystem.extend([str(in_count) for i in range(int(inp[i]))])
    try:
        filesystem.extend(list("." * int(inp[i+1])))
    except:
        break
    in_count += 1
while True:
    try:
        filesystem[filesystem.index(".")] = filesystem[-1]
    except:
        break
    filesystem.pop()
total = 0
for i in range(len(filesystem)):
    total += i * int(filesystem[i])
print(total)
