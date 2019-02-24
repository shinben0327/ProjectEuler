"""
Created on Feb 18 2019
@author: jihwanshin

Project Euler Problem 17
Number letter counts
https://projecteuler.net/problem=17
"""

units = {0: "", 1: "one", 2: "two", 3: "three", 4: "four",
         5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
tens = {0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "forty",
        5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def one_digit(num):
    strnum = str(num)
    inwords = ""
    if len(strnum) == 1:
        for i in range(1, 10):
            if num == i:
                inwords = units[num]
    return inwords


def two_digit(num):
    strnum = str(num)
    inwords = ""
    if len(strnum) == 2:
        if int(strnum[0]) == 1:
            if int(strnum[1]) == 0:
                inwords = "ten"
            if int(strnum[1]) == 1:
                inwords = "eleven"
            if int(strnum[1]) == 2:
                inwords = "twelve"
            if int(strnum[1]) == 3:
                inwords = "thirteen"
            if int(strnum[1]) == 4:
                inwords = "fourteen"
            if int(strnum[1]) == 5:
                inwords = "fifteen"
            if int(strnum[1]) == 6:
                inwords = "sixteen"
            if int(strnum[1]) == 7:
                inwords = "seventeen"
            if int(strnum[1]) == 8:
                inwords = "eighteen"
            if int(strnum[1]) == 9:
                inwords = "nineteen"
        if int(strnum[0]) == 2:
            inwords = "twenty" + units[int(strnum[1])]
        if int(strnum[0]) == 3:
            inwords = "thirty" + units[int(strnum[1])]
        if int(strnum[0]) == 4:
            inwords = "forty" + units[int(strnum[1])]
        if int(strnum[0]) == 5:
            inwords = "fifty" + units[int(strnum[1])]
        if int(strnum[0]) == 6:
            inwords = "sixty" + units[int(strnum[1])]
        if int(strnum[0]) == 7:
            inwords = "seventy" + units[int(strnum[1])]
        if int(strnum[0]) == 8:
            inwords = "eighty" + units[int(strnum[1])]
        if int(strnum[0]) == 9:
            inwords = "ninety" + units[int(strnum[1])]
    return inwords


def three_digit(num):
    strnum = str(num)
    inwords = ""
    if len(strnum) == 3:
        if len(str(int(strnum[1:3]))) == 2:
            inwords = one_digit(int(strnum[0])) + "hundredand" + two_digit(int(strnum[1:3]))
        if len(str(int(strnum[1:3]))) == 1 and int(strnum[1:3]) != 0:
            inwords = one_digit(int(strnum[0])) + "hundredand" + one_digit(int(strnum[1:3]))
        if len(str(int(strnum[1:3]))) == 1 and int(strnum[1:3]) == 0:
            inwords = one_digit(int(strnum[0])) + "hundred"
    return inwords


def four_digit(num):
    strnum = str(num)
    inwords = ""
    if len(strnum) == 4:
        if len(str(int(strnum[1:4]))) == 3:
            inwords = one_digit(int(strnum[0])) + "thousand" + three_digit(int(strnum[1:4]))
        if len(str(int(strnum[1:4]))) == 2:
            inwords = one_digit(int(strnum[0])) + "thousand" + two_digit(int(strnum[1:4]))
        if len(str(int(strnum[1:4]))) == 1 and int(strnum[1:4]) != 0:
            inwords = one_digit(int(strnum[0])) + "thousand" + one_digit(int(strnum[1:4]))
        if len(str(int(strnum[1:4]))) == 1 and int(strnum[1:4]) == 0:
            inwords = one_digit(int(strnum[0])) + "thousand"
    return inwords


def num_to_word(num):
    strnum = str(num)
    inwords = ""
    if len(strnum) == 1:
        for i in range(1, 10):
            if num == i:
                inwords = units[num]
    if len(strnum) == 2:
        if int(strnum[0]) == 1:
            if int(strnum[1]) == 0:
                inwords = "ten"
            if int(strnum[1]) == 1:
                inwords = "eleven"
            if int(strnum[1]) == 2:
                inwords = "twelve"
            if int(strnum[1]) == 3:
                inwords = "thirteen"
            if int(strnum[1]) == 4:
                inwords = "fourteen"
            if int(strnum[1]) == 5:
                inwords = "fifteen"
            if int(strnum[1]) == 6:
                inwords = "sixteen"
            if int(strnum[1]) == 7:
                inwords = "seventeen"
            if int(strnum[1]) == 8:
                inwords = "eighteen"
            if int(strnum[1]) == 9:
                inwords = "nineteen"
        if int(strnum[0]) == 2:
            inwords = "twenty" + units[int(strnum[1])]
        if int(strnum[0]) == 3:
            inwords = "thirty" + units[int(strnum[1])]
        if int(strnum[0]) == 4:
            inwords = "forty" + units[int(strnum[1])]
        if int(strnum[0]) == 5:
            inwords = "fifty" + units[int(strnum[1])]
        if int(strnum[0]) == 6:
            inwords = "sixty" + units[int(strnum[1])]
        if int(strnum[0]) == 7:
            inwords = "seventy" + units[int(strnum[1])]
        if int(strnum[0]) == 8:
            inwords = "eighty" + units[int(strnum[1])]
        if int(strnum[0]) == 9:
            inwords = "ninety" + units[int(strnum[1])]
    if len(strnum) == 3:
        if len(str(int(strnum[1:3]))) == 2:
            inwords = one_digit(int(strnum[0])) + "hundredand" + two_digit(int(strnum[1:3]))
        if len(str(int(strnum[1:3]))) == 1 and int(strnum[1:3]) != 0:
            inwords = one_digit(int(strnum[0])) + "hundredand" + one_digit(int(strnum[1:3]))
        if len(str(int(strnum[1:3]))) == 1 and int(strnum[1:3]) == 0:
            inwords = one_digit(int(strnum[0])) + "hundred"
    if len(strnum) == 4:
        if len(str(int(strnum[1:4]))) == 3:
            inwords = one_digit(int(strnum[0])) + "thousand" + three_digit(int(strnum[1:4]))
        if len(str(int(strnum[1:4]))) == 2:
            inwords = one_digit(int(strnum[0])) + "thousand" + two_digit(int(strnum[1:4]))
        if len(str(int(strnum[1:4]))) == 1 and int(strnum[1:4]) != 0:
            inwords = one_digit(int(strnum[0])) + "thousand" + one_digit(int(strnum[1:4]))
        if len(str(int(strnum[1:4]))) == 1 and int(strnum[1:4]) == 0:
            inwords = one_digit(int(strnum[0])) + "thousand"
    return inwords


final = ""
for number in range(1, 1001):
    final += num_to_word(number)
print(len(final))

# answer = 21124
