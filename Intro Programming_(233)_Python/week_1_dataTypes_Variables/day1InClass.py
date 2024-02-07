# DAY 1 (1/30/24) 

# Notes:
# SUBMIT FILE NAME LIKE THIS: FA2022-INFO233-01-Homework1-Your_Last_Name

# RUN PYTHON THROUGH --> TERMINAL BY RIGHT-CLICKING AND "RUN PYTHON"

# myInput = input("what is your name?")
# print("hello!,", myInput)

# myNumber = input("please input a number between 1 and 10")

# myNewNumber = myNumber * 5

# will log the string "5" five times: 55555
# myNewInteger = int(myNumber)

# myNewInterger will no log as a number because we change the dataType to an INT
# myNewNumber = myNewInteger * 5

# Taking the 'myNewInteger' variable which is now an integer, the terminal will log ('users string we turned into number' * 5)

# print("the INT result", myNewInteger)

# print('the STRING result', myNumber)

# print('the number(integer) result of multiplication', myNumber)

# WEEK-1 IN-CLASS ASSIGNMENT:

# -*- coding: utf-8 -*-
############ Challenge 1 ######################
# Calculate the number of decades of a person's age we want to see how many decades a person has lived and also how many years above the decade. 
# Start by assigning a number not ending in zero to a variable age.  This will be the person's age.
# Next Calculate decades by dividing the variable for a person's age using integer division
# Calculate the remaining years by dividing the variable for a person's age by 10 using modular division
# Finally, print out the decades and the remaining years. convert the decades and years to type string

""" Expected Output given 53 is the number your variable references
You are 5 decades and 3 years old.
"""

usersAge = 53
usersAgeAsYears = usersAge % 10
usersAgeAsDecades = usersAge // 10
# usersAgeAsNumber = int(usersAge)
print("you are", usersAgeAsDecades, "decades and", usersAgeAsYears, " years old!!")
# WILL LOG `you are 5 decades and 3 years old`

############ Challenge 2 ######################
#now modify the code so it asks a user for the age. ##HINT - reseach the function input()

""" Expected Output
What age do you want to determine the decades? 67
You are 6 decades and 7 years old.
"""

usersAge = input("Enter Your Age")
usersAgeAsNumber = int(usersAge)
usersAgeAsDecades = usersAgeAsNumber // 10
# MODULAR DIVISION = % (GIVES YOU THE DECIMAL AS WHOLE NUMBER);
usersAgeAsYears = usersAgeAsNumber % 10

print("you are", usersAgeAsDecades, "decades and", usersAgeAsYears, " years!!" )
# WILL LOG `you are ${usersAgeAsDecades} decades and ${usersAgeAsYears} years old`



# ALTERNATIVELY:
usersAge = int(input("Enter Your Age"))
usersAgeAsDecades = usersAge // 10
# MODULAR DIVISION = % (GIVES YOU THE DECIMAL AS WHOLE NUMBER);
usersAgeAsYears = usersAge % 10

print("you are", usersAgeAsDecades, "decades and", usersAgeAsYears, " years!!" )
# WILL LOG `you are ${usersAgeAsDecades} decades and ${usersAgeAsYears} years old`