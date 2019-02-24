"""
Created on Jan 17 2019
@author: jihwanshin

Project Euler Problem 1
Multiples of 3 and 5
https://projecteuler.net/problem=1
"""

sum_total = 0
for i in range(1000):
    if i % 3 == 0:
        sum_total += i
    if i % 5 == 0:
        sum_total += i
    if i % 15 == 0:
        sum_total -= i

print(sum_total)

#answer = 233168