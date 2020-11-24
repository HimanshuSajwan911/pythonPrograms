import random

array = []
target = int(input("Enter target number: "))

# This for loop adds random numbers to the array
for number in range(0, 50):
    rand_int = random.randint(-50, 50)
    array.append(rand_int)

print(sorted(array))

# This function finds the middle number of the array
def middleNumber(input_array):
    middle = float(len(input_array)) / 2
    if middle % 2 != 0:
        return input_array[int(middle - .5)]
    else:
        return input_array[int(middle)]

#Use while loop to check if outpu is equal to target or not.

for number in range(0, len(array)):
    if target < middleNumber(array):
        for i in

print(middleNumber(array).index())