"""
Created on Jan 20 2019
@author: jihwanshin

Project Euler Problem 6
Sum square difference
https://projecteuler.net/problem=6
"""

sum_of_squares = 0
sum_of_numbers = 0
for i in range(1, 101):
    sum_of_squares += i**2
    sum_of_numbers += i
square_of_sum = sum_of_numbers**2

difference = square_of_sum - sum_of_squares
print(difference)

# answer = 25164150
