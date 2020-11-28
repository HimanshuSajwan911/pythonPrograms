###############################################
#                                             #
#       Author UjjwalSharma 28/11/2020        #
#               Version 1.0                   #
#               							  #
###############################################

from itertools import permutations
from collections import Counter
import functools
# Added delay to make it look cooler ;)
import time
# while checked != password:
#     for i in range(0, int(len(password))):
#         for j in range(0, int(len(password))):
#             checked += characters[i]
#
#     print(checked)

# This function is seperated because you can add more characters
def charactersAsList():
    stringOfCharacters = "abcdefghijklmnopqrstuvwxyz"

    listOfCharacters = []

    for element in stringOfCharacters:
        listOfCharacters += element



    return listOfCharacters

def printListAsString(listPassword):
    password = ""
    for element in listPassword:
        password += element
    return password

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


def findThisPass(stringPassword):
    listPassword = []
    listOfCharacters = charactersAsList()
    #
    for element in stringPassword:
        listPassword += element

    perms = permutations(listOfCharacters, int(len(stringPassword)))

    for i in list(perms):
        time.sleep(0.001)
        if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, i, listPassword), True) :
        # if Counter(i) == Counter(listPassword):
            print(i)
            break
        else:
            print(i)


    # checkedPassword = []
    # while checkedPassword != listPassword:
    #     checkedPassword = []
    #     for i in range(0, int(len(listPassword))-1):
    #         for j in range(0, int(len(listOfCharacters))-1):
    #             checkedPassword[i] = listOfCharacters[j]
    #
    #     printListAsString(checkedPassword)

if __name__ == "__main__":

    password = input("Enter password : ")

    findThisPass(password)
