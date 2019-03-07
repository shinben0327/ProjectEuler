"""
Created on Feb 1 2019
@author: jihwanshin

Project Euler Problem 12
Highly divisible triangular number
https://projecteuler.net/problem=12
"""

while True:
    term = 1
    number = int((term + (term+1))/2)
    divisors_count = 0
    for i in range(1, number+1):
        if number % i == 0:
            divisors_count += 1
    if divisors_count > 500:
        print(number)
        break
    term += 1
