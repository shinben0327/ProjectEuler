"""
Created on Jan 20 2019
@author: jihwanshin

Project Euler Problem 9
Special Pythagorean triplet
https://projecteuler.net/problem=9
"""

# solution found from https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p009.py?ts=4

for a in range(1, 1001):
    for b in range(a, 1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a*b*c)
            break

# answer = 31875000
