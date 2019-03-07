"""
Created on Feb 21 2019
@author: jihwanshin

Project Euler Problem 25
1000-digit Fibonacci number
https://projecteuler.net/problem=25
"""

fibonacci = [1, 1]
while len(str(fibonacci[-1])) < 1000:
    next_term = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_term)
print(len(fibonacci))

# answer = 4782
