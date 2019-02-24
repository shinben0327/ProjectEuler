"""
Created on Feb 10 2019
@author: jihwanshin

Project Euler Problem 16
Power digit sum
https://projecteuler.net/problem=16
"""

the_number = str(2**1000)
total = 0

for digit in the_number:
    total += int(digit)

print(total)

# answer = 1366