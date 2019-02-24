"""
Created on Feb 20 2019
@author: jihwanshin

Project Euler Problem 22
Names scores
https://projecteuler.net/problem=22

p022names.txt can be downloaded below:
https://projecteuler.net/project/resources/p022_names.txt
"""

scores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
          'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
          't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

with open('p022names.txt', 'r') as names:
    names_string = names.read()
    names_list = names_string.split(",")

total = 0
index = 0
while index < len(names_list):
    name_strip = names_list[index].strip("\"")
    characters = list(name_strip)
    alphabetical_value = 0
    for character in characters:
        alphabetical_value += scores[character.lower()]
    total += alphabetical_value*(index+1)
    index += 1

print(total)
print(names_list.index("\"COLIN\""))
print(len(names_list))