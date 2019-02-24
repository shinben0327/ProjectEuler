"""
Created on Feb 24 2019
@author: jihwanshin

Project Euler Problem 5
Smallest multiple
https://projecteuler.net/problem=5
"""

# had to use the formula lcm(a, b) = a*b / gcd(a, b) from the internet

from math import gcd

lcm = 1
for i in range(2, 21):
    lcm = lcm * i / gcd(int(lcm), i)
print(lcm)

# answer = 232792560
