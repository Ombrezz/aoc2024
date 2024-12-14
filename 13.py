f = open("13.in")

problems = []

for line in f.readlines():
    a = line.split(": ")
    b = list(map(int, a[1].split()))
    problems.append((int(a[0]),b))

def bob_and_weave(a, b):
    ret = ""
    for i in range(len(a)):
        if i == len(a) - 1:
            ret += str(a[i])
            return ret
        ret += str(a[i]) + b[i]
total = 0
for problem in problems:
    inputs = problem[1]
    for i in range(2**(len(inputs)-1)):
        ops = []
        a = str(bin(i)).removeprefix("0b")
        a = a.rjust((len(inputs)-1), "0")
        for j in a:
            if j == "0":
                ops.append(")+")
            if j == "1":
                ops.append(")*")
        res = bob_and_weave(inputs, ops)
        res = ("(" * (len(a))) + res
        print(a)
        print(res)
        if eval(res) == problem[0]:
            total += problem[0]
            print("YUR")
            break
print(total)