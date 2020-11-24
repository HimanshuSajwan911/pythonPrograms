from collections import defaultdict

x = defaultdict(list)
y = defaultdict(list)

str = input().split()
mapObj = map(int, str)
lisOfInt = list(mapObj)

i = lisOfInt[0]
j = lisOfInt[1]

for m in range(0, i):
    x['lis1'].append(input())

for n in range(0, j):
    y['lis2'].append(input())

for g in x.items():
    for h in y.items():
        if g[1]
