"""
Created on Jan 26 2019
@author: jihwanshin

Project Euler Problem 7
10001st prime
https://projecteuler.net/problem=7
"""

# method using sieve of eratosthenes, however it is very inefficient
"""Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
Initially, let p equal 2, the smallest prime number.
Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n. - Wikipedia

def primeslist(n):
    primes = []
    def removeprimes(prime):
        for i in range(prime**2, n):
            if i % p == 0:
                try:
                    primes.remove(i)
                except ValueError:
                    continue
    for o in range(2, n):
        primes.append(o)
    p = 2
    while p < n:
        removeprimes(p)
        p += 1
    return primes

superprimes = primeslist(130000)
print(superprimes[10000])"""

# answer = 104743

# code taken from the internet which is way more efficient
# https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19
new_primes = []
for possiblePrime in range(2, 130000+1):
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        new_primes.append(possiblePrime)
print(new_primes[10000])

# made into function
"""def primeslist(number):
    primes = []
    for possiblePrime in range(2, number + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes"""
