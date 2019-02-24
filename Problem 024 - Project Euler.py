"""
Created on Feb 21 2019
@author: jihwanshin

Project Euler Problem 24
Lexicographic permutations
https://projecteuler.net/problem=24
"""

from jsmaths import factorial

indexp1 = 0
nums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

for fac in range(9, 0, -1):
    while indexp1 < 1000000:
        indexp1 += factorial(fac)
        nums[fac+1] += 1

millionth_num = 0
for i in range(10, 0, -1):
    millionth_num += nums[i]*10**(i-1)
print(millionth_num)
