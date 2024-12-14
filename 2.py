from collections import Counter
list1 = []
list2 = []
f = open("1.in")
for line in f.readlines():
    a = list(map(int, line.split()))
    list1.append(a[0])
    list2.append(a[1])
c = Counter(list2)
total = 0
for i in list1:
    total += i * c[i]
print(total)