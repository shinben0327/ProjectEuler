"""
Created on Feb 1 2019
@author: jihwanshin
"""

"""
This Python file will be used to store mathematical functions I made by myself. 
Type 'from jsmaths import X' to use the functions in other files. 
"""

def factorial(x):
    number = x
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

def npr(n, r):
    return int(factorial(n)/factorial(n-r))

def npir(n, r):
    return n ** r

def ncr(n, r):
    return int(factorial(n)/factorial(n-r)/factorial(r))

def nhr(n, r):
    return ncr(n+r-1, r)

def mean(array):
    total = 0
    for i in array:
        total += i
    return total / len(array)

def median(array):
    array.sort()
    if len(array) % 2 == 0:
        return (array[int(len(array)/2-1)] + array[int(len(array)/2)])/2
    else:
        return array[int((len(array)-1)/2)]
