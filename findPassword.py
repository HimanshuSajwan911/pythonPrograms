###############################################
#                                             #
#       Author UjjwalSharma 28/11/2020        #
#               Version 1.0                   #
#               							  #
###############################################

# ISSUES
# repeating elements give problem
# Program stops printing but resumes at some point again (I don't know why)

from itertools import permutations
# from collections import Counter   # Was used in findThisPass() to check equality of lists
import functools
# Added delay to make it look cooler ;)
import time

# This function is seperated because you can add more characters
def charactersAsList():
    # stringOfCharacters = "abcd"
    stringOfCharacters = "abcdefghijklmnopqrstuvwxyz"

    listOfCharacters = []

    for element in stringOfCharacters:
        listOfCharacters += element

    return listOfCharacters

def numbersAsList():
    stringOfNumbers = "0123456789"

    listOfNumbers = []

    for number in stringOfNumbers:
        listOfNumbers += number

    return listOfNumbers

# Takes any list as input and returns it in form of string
def ListToString(listPassword):
    password = ""
    for element in listPassword:
        password += element
    return password

# Takes any string as input and returns it in form of string
def stringToList(string):
    lis = []

    for element in string:
        lis += element

    return lis

# # This function prints all the substrings of the string given as input
# def substr(string):
#     n = int(len(string))
#     for Len in range(1, n+1):
#         for i in range(n-Len+1):
#             j = i + Len - 1
#
#             for k in range(i, j+1):
#                 print(stringOfCharacters[k], end="")
#             print()

# Using permutations to check all possible ways of arranging the characters
def findThisPassLetters(stringPassword):
    listPassword = []
    listOfCharacters = charactersAsList()
    #
    for element in stringPassword:
        listPassword += element

    perms = permutations(listOfCharacters, int(len(stringPassword)))

    for i in list(perms):
        # Enable sleep to see whats hapening
        time.sleep(0.001)
        if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, i, listPassword), True) :
        # if Counter(i) == Counter(listPassword):  # This didn't check the order of elements in list
            print(i)
            break
        else:
            print(i)


def findThisPassNumbers(stringPassword):
    listPassword = []
    listOfNumbers = numbersAsList()

    for element in stringPassword:
        listPassword += element

    perms = permutations(listOfNumbers, int(len(stringPassword)))

    for i in list(perms):
        # Enable sleep to see whats hapening
        time.sleep(0.001)
        if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, i, listPassword), True) :
        # if Counter(i) == Counter(listPassword):  # This didn't check the order of elements in list
            print(i)
            break
        else:
            print(i)

# Main loop
if __name__ == "__main__":

    password = input("Enter password : ")

    passwordAsList = stringToList(password)

    passHasInt = False

    for element in passwordAsList:
        i = 0
        if passwordAsList[i] in "0123456789":
            passHasInt = True
            i += 1

    if passHasInt:
        findThisPassNumbers(password)
    elif not passHasInt:
        findThisPassLetters(password)
    else:
        print("Sorry can't crack this one.")

    # functions used to find the password
    # findThisPassNumbers(password)
    # findThisPassLetters(password)
