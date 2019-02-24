"""
Created on Feb 10 2019
@author: jihwanshin

Project Euler Problem 20
Factorial digit sum
https://projecteuler.net/problem=20
"""

from jsmaths import factorial

the_number = str(factorial(100))
total = 0

for digit in the_number:
    total += int(digit)

print(total)

# answer = 648