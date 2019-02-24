"""
Created on Jan 26 2019
@author: jihwanshin

Project Euler Problem 10
Summation of primes
https://projecteuler.net/problem=10
"""

# code taken from the internet which is way more efficient than my own idea
# https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19

counter = 0
for possiblePrime in range(2, 2000000+1):
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        counter += possiblePrime
print(counter)

# answer = 142913828922
