"""
Created on Feb 21 2019
@author: jihwanshin

Project Euler Problem 24
Lexicographic permutations
https://projecteuler.net/problem=24
"""

from jsmaths import factorial

nums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

million = 1_000_000
for i in range(10, 0, -1):
    while million > factorial(i):
        million -= factorial(i)
        nums[i] += 1
for i in range(10, 0, -1):
    print(nums[i], end='')
# this printed 0266251211 which makes no sense...
