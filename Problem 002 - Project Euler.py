"""
Created on Jan 17 2019
@author: jihwanshin

Project Euler Problem 2
Even Fibonacci numbers
https://projecteuler.net/problem=2
"""

fibonacci = []
for i in range(2000000):
    if i == 0:
        fibonacci.append(1)
    if i == 1:
        fibonacci.append(2)
    if i > 1:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    if fibonacci[i] > 4000000:
        break

total_sum = 0
for i in fibonacci:
    if i % 2 == 0:
        total_sum += i

print(total_sum)

# answer = 4613732
