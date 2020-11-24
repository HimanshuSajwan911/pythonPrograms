n = int(input())
arr = input().split()

sizes = []
for i in range(0, n):
    sizes.append(int(arr[i]))

customers = int(input())
totMon = 0

for sale in range(0, customers):
    str = input().split()
    map_obj = map(int, str)
    ints = list(map_obj)
    size = ints[0]
    mon = ints[1]
    if size in sizes:
        totMon += mon
        sizes.remove(size)

print(totMon)
