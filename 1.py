list1 = []
list2 = []
print("a")
f = open("1.in")
for line in f.readlines():
    a = list(map(int, line.split()))
    list1.append(a[0])
    list2.append(a[1])
total = 0
while len(list1) > 0:
    a = min(list1)
    b = min(list2)
    total += abs(a - b)
    list1.remove(a)
    list2.remove(b)
    print(len(list1))
    print(len(list2))
print(total)