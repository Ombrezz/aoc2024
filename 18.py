import time
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
did_move = True
print(filesystem)
while did_move:
    if filesystem[-1] == ".":
        break
    for search in range(int(filesystem[-1]), -1, -1):
        print(search)
        did_move = False
        ind = filesystem.index(str(search))
        final = len(filesystem) - list(reversed(filesystem)).index(str(search))
        best_contig = (0,0)
        curr_contig = 0
        curr_contig_i = 0
        found_contig = False
        for i in range(len(filesystem)):
            if filesystem[i] == "." and not found_contig:
                curr_contig = 1
                curr_contig_i = i
                found_contig = True
                continue
            if filesystem[i] == "." and found_contig:
                curr_contig += 1
                continue
            if filesystem[i] != ".":
                found_contig = False
                if curr_contig >= final-ind:
                    best_contig = (curr_contig_i, curr_contig)
                    break
        if best_contig != (0,0) and best_contig[0] < ind:
            made_change = True
            for i in range(best_contig[0], best_contig[0]+(final-ind)):
                filesystem[i] = str(search)
            for i in range(ind, final):
                filesystem[i] = "."
            did_move = True
print("".join(filesystem))
total = 0
for i in range(len(filesystem)):
    if filesystem[i] != ".":
        total += i * int(filesystem[i])
print(total)
