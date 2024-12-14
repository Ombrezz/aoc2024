f = open("13.in")

problems = []

for line in f.readlines():
    a = line.split(": ")
    b = list(map(int, a[1].split()))
    problems.append((int(a[0]),b))

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

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
    for i in range(3**(len(inputs)-1)):
        ops = []
        a = ternary(i)
        a = a.rjust((len(inputs)-1), "0")
        #paren_count = 0
        for j in a:
            if j == "0":
                #paren_count += 1
                ops.append("+")
            if j == "1":
                #paren_count += 1
                ops.append("*")
            if j == "2":
                ops.append("||")
        #res = bob_and_weave(inputs, ops)
        #res = ("(" * paren_count) + res
        #print(a)
        #print(res)
        #res = res.replace("||", "")
        # if eval(res) == problem[0]:
        #     total += problem[0]
        #     print(problem)
        #     break
        final = inputs[0]
        for i in range(1, len(inputs)):
            if ops[i-1] == "+":
                final += inputs[i]
            elif ops[i-1] == "*":
                final *= inputs[i]
            elif ops[i-1] == "||":
                final = str(final) + str(inputs[i])
            final = int(final)
        if final == problem[0]:
            total += problem[0]
            print(problem)
            break
print(total)