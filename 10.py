from collections import defaultdict

f = open("9.in")

is_lesser_than = defaultdict(list)
is_greater_than = defaultdict(list)
docs = []
sum = 0

for line in f.readlines():
    if "|" in line:
        a,b = list(map(int, line.split("|")))
        is_lesser_than[a].append(b)
        is_greater_than[b].append(a)
    else:
        docs.append(list(map(int, line.split(","))))
bad_docs = []

for doc in docs:
    good_doc = True
    for page in doc:
        lesser = is_lesser_than[page]
        greater = is_greater_than[page]
        good_lesser = True
        for item in lesser:
            if item in doc:
                if doc.index(item) < doc.index(page):
                    good_lesser = False
        good_greater = True
        for item in greater:
            if item in doc:
                if doc.index(item) > doc.index(page):
                    good_greater = False
        if not (good_greater and good_lesser):
            good_doc = False
    if not good_doc:
        bad_docs.append(doc)
for doc in bad_docs:
    did_fix = True
    while did_fix:
        did_fix = False
        for page in doc:
            lesser = is_lesser_than[page]
            greater = is_greater_than[page]
            for item in lesser:
                if item in doc:
                    if doc.index(item) < doc.index(page):
                        temp = doc[doc.index(page)]
                        doc[doc.index(page)] = doc[doc.index(item)]
                        doc[doc.index(item)] = temp
                        did_fix = True
                        break
            for item in greater:
                if item in doc:
                    if doc.index(item) > doc.index(page):
                        temp = doc[doc.index(page)]
                        doc[doc.index(page)] = doc[doc.index(item)]
                        doc[doc.index(item)] = temp
                        did_fix = True
                        break
sum = 0
for doc in bad_docs:
    sum += doc[int((len(doc)-1)/2)]
print(sum)