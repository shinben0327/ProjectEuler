"""
Created on Jan 20 2019
@author: jihwanshin

Project Euler Problem 4
Largest palindrome product
https://projecteuler.net/problem=4
"""

palindromes = []
for i in range(100, 1000):
    for o in range(100, 1000):
        product = str(i*o)
        palindromes.append(int(product))
        length = len(product)
        for p in range(len(product)):
            if product[p] != product[length-p-1]:
                palindromes.remove(int(product))
                break
print(max(palindromes))

# answer = 906609
