"""
Created on Feb 1 2019
@author: jihwanshin

Project Euler Problem 14
Longest Collatz sequence
https://projecteuler.net/problem=14
"""

# change date
def collatz(num):
    thenum = num
    sequence = []
    sequence.append(thenum)
    while thenum != 1:
        if thenum % 2 == 0:
            thenum = thenum / 2
            sequence.append(thenum)
        if thenum % 2 == 1:
            thenum = 3*thenum + 1
            sequence.append(thenum)
    return len(sequence)

print(collatz(13))
"""maximum = float("-inf")
for num in range(900001, 1000000, 2):
    if collatz(num) > maximum:
        maximum = num
print(maximum)"""
