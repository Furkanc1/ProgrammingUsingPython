# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 07:56:33 2022

@author: john
"""

# Course: Introduction to Programming (INFO-233)
# Student Name: 

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

################################
# Problem 1: Lists
################################

# Build a list (called myList) that contains every year from 2015 to 2022. Write
# the code to verify whether index 1 is (or is not) a leap year. Also verify
# whether the last index of myList is a leap year.
# (Hint: leap years are evenly-divisible by 4)

# with the way i wrote this code we technically dont even need a list, but rather for the sake of answering the actual questions
selectedYear = int(input("select a year from my list to see if it is a leap year!"))
# % is an operator which returns what remains of two divided numbers
# in this case if the selected year is % by 4, AND == to 0 meaning the remainder is 0, then it will be TRUE, other wise it will run the else
leapYearEquation = selectedYear % 4 == 0

if leapYearEquation:
    print(f"{selectedYear} is indeed a Leap Year! ")
else:
    print(f"{selectedYear} is NOT a leap year! ")


# WHAT I WAS ACTUALLY SUPPOSED TO ANSWER: (didnt realize it was just a matter of selecting 2 index's)

myList = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
selectedIndexYear = myList[1] % 4 == 0
if selectedIndexYear:
    print(f"{myList[1]} IS a leap year!")
else:
    print(f"{myList[1]} is NOT leap year!")

lastSelectedIndexYear = myList[-1] % 4 == 0
if lastSelectedIndexYear:
    print(f"{myList[-1]} IS a leap year!")
else:
    print(f"{myList[-1]} is NOT leap year!")

########################
# Problem 2: Sets
########################

# Using the two sets below, divBy2 and divBy3, determine which values occur in
# both sets and assign that to a variable called common. Then confirm whether
# common is in fact a subset of both divBy2 and divBy3.

divBy2 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
divBy3 = {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

# intersection = what is common between the two sets
common = (divBy2).intersection(divBy3)

# difference = what is in one set but is not in another (depends on which set you place first in the method)
uncommonFrom2To3 = (divBy2).difference(divBy3)
uncommonFrom3To2 = (divBy3).difference(divBy2)


print(common)
print(uncommonFrom2To3)
print(uncommonFrom3To2)