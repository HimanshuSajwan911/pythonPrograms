import random

arr = [4, 32, 104, 111, 121, 131, 141, 161, 17, 345, 333, 917, 228, 282, 497, 11]

min_val = 100
max_val = 300

print(arr)
print()


# for index in range(len(arr) - 1, -1, -1):
#     if arr[index] >= max_val or arr[index] <= min_val:
#         print(index, arr)
#         del arr[index]

top_index = len(arr) - 1
# The same thing but with the reversed function.
for index, value in enumerate(reversed(arr)):
    if value < min_val or value > max_val:
        del arr[top_index - index]
        print(top_index - index, value)
