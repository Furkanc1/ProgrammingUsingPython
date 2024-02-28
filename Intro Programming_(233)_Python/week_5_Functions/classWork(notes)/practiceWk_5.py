# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:57:55 2022

@author: johnk
"""
## Challenge 1 #####################
# Create a function which asks a user to type a season, spring, summer , fall, winter.
# Depending on which season they type, print a seasonal statement. CAll the function
# by passing the variable holding the user's season. Please ensure the inout is not case-sensitive. 
# For example Winter is the same as winter is the same as WINTER.
# also inlcude a print statement if the user entered a word which is not a season. 
# Output messages as follows
# for Spring,  "April showers bring May Flowers"
# For Summer, "It's Beach time"
# For Fall, "It's time for Turkey Day"
# For Winter, "Snowman Season"
# For an incorrect season, "Plese enter either Spring, Summer, Winter or Fall"

"""
Expected Output

please enter a season for a message SPRING
April showers bring May Flowers

please enter a season for a message Spring
April showers bring May Flowers

please enter a season for a message spring
April showers bring May Flowers

please enter a season for a message pre spring
Plese enter either Spring, Summer, Winter or Fall

"""

def seasons(season):
    if (season == "fall"):
        print("It's time for Turkey Day")
    elif (season == "spring"):
        print("April showers bring May Flowers")
    elif (season == "winter"):
        print("Snowman Season")
    elif (season == "summer"):
        print("It's Beach time")
    else:
        print("You must input either, 'spring', 'summer', 'winter', or 'fall'")
        askUser()


# CASEFOLD basically disregards case sensitivity? but i think the best practice for real world applications would be .lower() or .upper() to account or adjust for user input error
    
def askUser():
    selectedSeason = str(input("Choose a season for a message!")).casefold()
    seasons(selectedSeason)

askUser()
    
## Challenge 2 #####################
# Error Handling
# Practice error handling by writing a function to print the square of an integer and return the square
# to the main part of the program and print it out. If the user should enter a decimal (float) in error,
# let the user know to only enter a whole nmuber (integer) the program should run and not generate any 
#system errors. 

""" Expected Output
Please enter an integer to get its square root: 10
The square of  10 is 100

Please enter an integer to get its square root: 2.3
Your entry was not a whole number, please enter an whole number

Please enter an integer to get its square root: go away
Your entry was not a whole number, please enter an whole number


"""
import math

def squareRoot(integer):
    squareRootEquation = round(math.sqrt(integer), 3)
    print(f"The square root of {integer} is {squareRootEquation}")

def askUserForNumber():
    try:
        numberToSqrt = int(input("Enter a number to find its square root! "))
        squareRoot(numberToSqrt)
    except ValueError:
        print("Input MUST be an INTEGER")
        askUserForNumber()

askUserForNumber()



## Challenge 3 #####################
# Combining what we learned
# we've learned a lot over the last few weeks. Let's put that to use
# Create a code block which consists for a function to average grades
#The function should be able to take any number of grades
# Caluclate the average of the grades and return it to the main prgram
# in the main program use the average returned and test it to determine a letter grade
# 90 and up is A, 80 to 89 is a B, 70 to 79 is a C 60 to 69 a D and below 60 is an F.

##HINT, you tested for grades before, right, reuse the code.  Code resuse is one of the best ways to 
#things done quickly

""" Expected Output  given 100,100,70,60
Your grade averages is 82.5
which is a B
"""

# # convert each item to int type
# for i in range(len(user_list)):
#     # convert each item to int type
#     user_list[i] = int(user_list[i])
def averageOutGrade(*arg):
    for x in arg:
        averageOfGrades = sum(arg) / len(arg)
    print(f"Your average grade is: {averageOfGrades}")
    return averageOfGrades
gradeAverage = averageOutGrade
# def letterGrade():

    
def askUserForGrades():
    usersGrades = input("Enter your grades! (ex: 100, 96, 35, 44, etc...) ").split()

    usersGradesAsInt = [int(grade) for grade in usersGrades]
    averageOutGrade(*usersGradesAsInt)

averageGradeAsVariable = askUserForGrades()

if averageGradeAsVariable >= 90:
    print(f"{averageGradeAsVariable} is an A")
elif 80 <= averageGradeAsVariable <= 89:
    print(f"{averageGradeAsVariable} is a B")
elif 70 <= averageGradeAsVariable <= 79:
    print(f"{averageGradeAsVariable} is a C")
elif 60 <= averageGradeAsVariable <= 69:
    print(f"{averageGradeAsVariable} is a D")
elif averageGradeAsVariable <= 59:
    print(f"{averageGradeAsVariable} is a FAILING GRADE")
else:
    print("Error in user input")
