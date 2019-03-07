"""
Created on Mar 7 2019
@author: jihwanshin

Project Euler Problem 28
Number spiral diagonals
https://projecteuler.net/problem=28
"""

total = 0
number = 1
total += number
for i in range(1, 501):  # there are 500 squares loops that go around
    for j in range(4):  # four numbers that are diagonals in each square loop
        number += 2*i  # this is the pattern of the diagonal numbers
        total += number
print(total)

# answer = 669171001
