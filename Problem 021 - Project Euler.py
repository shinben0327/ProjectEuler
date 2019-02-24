"""
Created on Feb 20 2019
@author: jihwanshin

Project Euler Problem 21
Amicable numbers
https://projecteuler.net/problem=21
"""


def d(n):
    total = 0
    for num in range(1, n):
        if n % num == 0:
            total += num
    return total


thetotal = 0
for i in range(1, 10000):
    if i == d(d(i)):
        thetotal += i
print(thetotal)
