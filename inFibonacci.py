# In this code you have to enter any integer and the program will tell you if
# the number exists in the fibonacci series or not.

# A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 – 4)
# is a perfect square (Source: Wiki).

import math

# This function returns true if the given number is a perfect square.
def isPerfectSquare(f):
    s = int(math.sqrt(f))
    return s*s == f

# This function can be used to print the fibonacci element of the index user
# inputs, whereas this function is not being used in this program.
def printFibonacci(x):

    i = 0
    m = 0
    n = 1
    for i in range(x - 1):
        element = m + n
        m = n
        n = element

    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return element

# This function tells if the given number exists in the fibonacci series or not.
def inFibonacci(n):
    x = isPerfectSquare(5*n*n + 4)
    y = isPerfectSquare(5*n*n - 4)
    if x == True or y == True:
        print("Yes, number exists in the fibonacci series.")
    else:
        print("No, number dosen't exist in fibonacci series.")

# Main function, only for input and output and basic conditions.
if __name__ == "__main__":
        numberToCheck = int(input("Enter the number to check in the fibonacci : "))
        inFibonacci(numberToCheck)
