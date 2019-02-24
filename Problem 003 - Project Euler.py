"""
Created on Jan 18 2019
@author: jihwanshin

Project Euler Problem 3
Largest prime factor
https://projecteuler.net/problem=3
"""

num = 600851475143

for i in range(2, num):
    while num % i == 0:
        num = num / i
    if num == 1:
        print(i)
        break

#answer = 6857

#ALL THE CODES THAT I FAILED BECAUSE OF INEFFICIENCY

#find primes, check if primes are factors of the number. if it is print the max
"""primes = []
for i in range(2, 600851475143):
    primes.append(i)
    for n in range(2, i):
        if i % n == 0:
            primes.remove(i)
            break

prime_factors = []
for i in primes:
    if 600851475143 % i == 0:
        prime_factors.append(i)

print(max(prime_factors))"""

#divide the number and if the modulo is zero, it is a factor. iterate until the largest number is found
"""prime_factors = []
largest_prime_factor = 0
num = 600851475143
for i in range(2, num):
    if num % i == 0:
        if i > largest_prime_factor:
            largest_prime_factor = i
        num = num/i
    else:
        continue
print(max(prime_factors))"""

#find factors. check if factors are prime numbers, if it is print the max
"""factors = []
for i in range(2, 600851475143):
    if 600851475143 % i == 0:
        factors.append(i)
for i in factors:
    for n in range(2, i):
        if i % n == 0:
            factors.remove(i)
            break
print(factors[0])"""
