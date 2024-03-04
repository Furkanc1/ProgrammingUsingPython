# Course: Introduction to Programming (INFO-233)
# Student Name: 

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

##############
# Problem 1
##############

# Combining what we learned
# we've learned a lot over the last few weeks. Let's put that to use
# Create a code block which consists of a function to average grades and a function to assign a letter grade
# to the average returned by your function

#The average function should be able to take any number of grades
# Use two for loops to calculate the average of the grades and return it to the main program. One loop calculates
# how many grades are to be averaged and the second sums the grades. 
# use the function you previously creeated to assign a letter grade to the average by passing the 
# returned average to your letter grade function and print out the number grade to two deciamal places and the letter grade
#Use 100.100.70.60 as the input to the function

##HINT, you tested for grades before, right, reuse the code.  Code resuse is one of the best ways to 
#things done quickly
""" Expected Output

Your average is 82.5
Your final grade is B
"""
# function takes in *grades as Arg
def averageOfGradesInList(*grades):
    # Preset the value for how many grades are in the list (ex: list = 100, 200, 300 || So, the total amount of grades is 3!)
    numbersOfGradesInputtedByUser = 0
    # preset the value for the total SUM of the grades (EX: grades in list = 100, 200, 300 || So, total of Grades in the list = 600)
    sumOfGradeNumbersInList = 0

    # loop through each number in the list, and add 1 to the total number of values we preset (every time)
    for eachValueOfList in grades:
        numbersOfGradesInputtedByUser += 1

    # also loop through each grade adding the grades up and redifining "sumOfGradeNumbersInList" every single time it loops 
        # EX:GradesInList = 100, 200, 300 ("sumOfGradesNumberList = 0" || "sumOfGrades" += "gradesInList" || output: 0 + 100 ||LOOP 2: "sumOfGrades" += "gradesInList" || output: 100 + 200 ||LOOP 3: "sumOfGrades" += "gradesInList" || output: 300 + 300)
    #  Which would finally return: 600 as the total.)
    for sumOfGrades in grades:
        sumOfGradeNumbersInList += sumOfGrades
    # Finally we do simple math to find the average, SUM of numbers(600) / total amount of values in list (3) = average of __ (in my example 200 would be the output)
    averageOfGrade = round((sumOfGradeNumbersInList / numbersOfGradesInputtedByUser), 2)
    # Return the average grade to use it for getting the LetterGrade
    return averageOfGrade

def letterGradeForListValues(averageFromOtherFunction):
    if averageFromOtherFunction >= 90:
        average = "A"
    elif averageFromOtherFunction >= 80:
        average = "B"
    elif averageFromOtherFunction >= 70:
        average = "C"
    elif averageFromOtherFunction >= 60:
        average = "D"
    else:
        average = "F"
    return average

listOFGrades = [100, 100, 70, 60]
averageGrade = averageOfGradesInList(*listOFGrades)
letterGrade = letterGradeForListValues(averageGrade)
pointsNeededToPass = (60 - averageGrade)

print(f"Your grade average is: {averageGrade}, Your correlating letter grade is: {letterGrade}")
    
##############
# Problem 2
##############

#Now that you get how to use a function , pass argumanets and return values, copy the code from above
# modify it so it takes input from a user, The input should be comma separated (each grade is separated by a comma)
# 
##HINT Remember, an input is always type string. You will have to convert the string input
# to a list of floats. Modify your averages function and replace the second for loop with the sum() function 
# to get the total of all of the grades. 


"""Expected Outout

Please enter grades separated by a comma (,)100,98.5,99.5,65.3,78.2,32.2,65
Your average is 76.96
Your final grade is C

"""

def averageOutGrade(*arg):
    averageOfGrades = round(sum(arg) / len(arg), 2)
    print(f"Your average grade is: {averageOfGrades}")
    gradeAverage = round(averageOfGrades, 2)
    return gradeAverage

# def letterGrade():
# takes in averageGrade parameter which is passed down below when the function is called
def letterGrade(averageGrade):
    failingByPoints = 60 - averageGrade
    # print(failingByPoints)
    # if the average grade given is >= 90 then theres two paths:
    # print statement AND DEFINE letterGrade variable as A
    if averageGrade >= 90:
        print(f"Your letter grade is: A")
        letterGrade = "A"
    # if the average grade given is >= 80 then theres two paths:
    # print statement AND DEFINE letterGrade variable as B
    elif averageGrade >=80:
        print(f"Your letter grade is: B")
        letterGrade = "B"
    # if the average grade given is >= 70 then theres two paths:
    # print statement AND DEFINE letterGrade variable as B
    elif averageGrade >=70:
        print(f"Your letter grade is: C")
        letterGrade = "C"
    # if the average grade given is >= 60 then theres two paths:
    # print statement AND DEFINE letterGrade variable as B
    elif averageGrade >=60:
        print(f"Your letter grade is: D")
        letterGrade = "D"
        # any other situation:
    # print statement AND DEFINE letterGrade variable as FAIL
    else:
        letterGrade = "F"
        print(f"Your letter grade is: {letterGrade}, you need {failingByPoints} points to pass!!")
        # we can use the letter grade variable that is returned as a variable in the "askUser" function, and log it in the print statement, rather than do a print statement on every line (either way works but variable method seems to be more efficient)
        return letterGrade

# Main Program Here:
def askUserForGrades():

    # asking the user to put their graades in
    try:
        usersGrades = input("Enter your grades! (ex: 100, 96, 35, 44, etc...) ").split(",")
    # we take users grades and convert them into INTEGERS
        usersGradesAsInt = [int(grade) for grade in usersGrades]
        print(f"Grades you entered: {usersGradesAsInt}")
    # AverageGrade variable is defined by what is returned by the averageOutGrade Function which takes in the users grades(converted to INT)
        averageGrade = averageOutGrade(*usersGradesAsInt)
    # similarly letter gradeValue variable is defined by the output for letterGrade() function which takes in whatever the average grade was
        letterGrade(averageGrade)
    except ValueError:
        print(f"{usersGrades} is not valid, must enter NUMBERS seperated with commas (,) (ex: 100, 200, 300, ...)")
        askUserForGrades()

    # Also we could do:

    # HERE IS WHERE WE UTILIZE letterGrade Variable from the letterGrade() function:

    # letterGradeVariable = letterGrade(averageGrade)
    # print(f"Your final grade is: {letterGradeVariable}")

    # however in this case we would have to remove the print statements from the original function "letterGrade()" i believe

askUserForGrades()




