# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:51:44 2023

@author: john
"""

"""
Welcome to the Mideterm for INFO-233

Directions: -  Credit for the problem will not be given without proper comments. All code must contain comments to explain your logic.
    1. Read through all of the comments in this file and follow the directions exactly. There are extra credit options in problems 2,3 & 4. Choose any 3 problems to complete for the exam
    2. Your code's output must match the expected output from each problem.
    3. Original work only. Your work must be your own. 
    4. When completed, save the file as info-233-midterm_yourlastname and uipload it the assignment in Canvas
    5. Good luck and relax. Use all of the resources you have. 
"""
############################################################ Problem 1  
## This problem convers the concepts of:
##      1. String Slicing
##      2. Len ()
##      3. Fstrings    
## Given the string below, write three lines of code to 
## 1. first display the string on the screen
## 2. Using one fstring, Extract the class name from the sting and display it as part of the second sentence 
## 3. Using one fstring, Create the third sentence by calculating how many characters on the screeen

""" Expected Output

This is the midterm for INFO-233
The class I am taking is INFO-233
The original string is 32 characters long

"""
print("\nProblem 1:\n")
## 1. first display the string on the screen
myString = "This is the midterm for INFO-233"
print(myString)
## 2. Using one fstring, Extract the class name from the sting and display it as part of the second sentence 
className = myString[24:-1]
print(f"The class I am taking is {className}")
## 3. Using one fstring, Create the third sentence by calculating how many characters on the screeen
lengthOfString = len(myString)
print(f"The original string is {lengthOfString} characters long")

############################################################ Problem 2  ############################################################################################
## This problem covers the concepts of:
##      1. Iteration using For loops
##      2. List creation
##      3. Data types
## Create two empty lists:
## iterate through a range of 25 numbers from 1 to  25 and add them to the first list
## Iterate through a range of 25 numbers from 26 to 50 and add them to the second list
## print out both lists and their types

""" ***************** Extra Credit is available if you complete this problem using only 1 loop to iterate over all 50 numbers to generate the expected output*****************"""
""" Expected Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] <class 'list'>
[26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50] <class 'list'>
"""
print("\nProblem 2:\n")

## Create two empty lists:

# here we created the first two lists assigned to nothing
listOne = []
# print(listOne)
listTwo = []

## iterate through a range of 25 numbers from 1 to  25 and add them to the first list

# Here we itterate through a range of numbers (1-25) and for every number, we append it to the list (populate the list)
for numbers in range(1,26):
    listOne.append(numbers)
    # finally OUTSIDE of the loop we print it (if it was inside we get [1], [1, 2] ... and so on till 25)
print(f"{listOne} -- {type(listOne)}")   

## Iterate through a range of 25 numbers from 26 to 50 and add them to the second list
for numbers in range(26,51):
    listTwo.append(numbers)
print(f"{listTwo} -- {type(listTwo)}")   
## print out both lists and their types (done)

# adding to new list means we need to combine the lists:
listOne.extend(listTwo)
print(f" \n The combines list is:\n {listOne} {type(listOne)}")

# EXTRA CREDIT:
# set empty list
extraCreditList = []
# same itteration through numbers 1-50
for numbers in range(1,51):
    extraCreditList.append(numbers)

# Here we create variables of the first 25 numbers using their index #
first25 = extraCreditList[0:24]
# same thing here for last 25 numbers (using index (starts at 0))
last25 = extraCreditList[25:49]
# print statement:
print(f"\n The Extra Credit List : \n{first25} + {type(first25)} \n {last25} + {type(last25)} \n ")


############################################################ Problem 3  ############################################################################################
## This problem convers the concepts of:
##      1. Dictionaries
##      2. fstrings
##      3. exception handling    
## Given the dictionary, write a section of code which: 
## 1. Ask a user to enter a month
## 2. Ensure that the month exists in the dictionary. If it does
## 3. Print out a sentence diplaying the month and the gemstone for the month
## 4.  if the user input is not in the dictionary, print a message to let them know
## and ask them to please enter a correct month
## your program should accept any version of case in the user's selection wihtout an error
""" Expected Output
if a user enters November

please enter a month of the year:november
The jewel for the month of November is Topaz

If a user enters something which is not a valid month

please enter a month of the year:jkdlfjlasdj;f
You entered an incorrect choice.
please enter a month of the year:November

"""

""" ***************** Extra Credit is available if you complete this problem by declaring a function which returns the month and its gemstone to the main part of the program
which calls out the funcation and prints out the statment 

"""

birthStones = {
    
    'January':'Garnet',
    'February':'Amethyst',
    'March':'Aquamarine',
    'April':'Diamond',
    'May':'Emerald',
    'June':'Pearl',
    'July':'Ruby',
    'August':'Peridot',
    'September':'Sapphire',
    'October':'Opal',
    'November':'Topaz',
    'December':'Tanzanite',
    }
# get user input and capatalize it
usersMonth = input("please enter a month of the year or `q` to quit! ").capitalize()

# if the users input is in the dictionary it will print the value(gem) based on the key(month)
if (usersMonth) in (birthStones):
    print(f"The BirthStone for the month of {usersMonth} is: {birthStones[usersMonth]}!")
# finally the else is if the users input was not found in the dictionary, will tell them their input was wrong
else:
    print(f"{usersMonth} is not the correct input!! Try again ")

    
# EXTRA CREDIT:
# define function to ask user
def askUser():
    print(f"\n  EXTRA CREDIT PORTION:  \n")
    # defiens users input and captializes the first letter to match dictionary
    usersMonth = input("please enter a month of the year or `q` to quit! ").capitalize()
    # if the users input is in the dictionary it will print the value(gem) based on the key(month)
    if (usersMonth) in (birthStones):
        print(f"The BirthStone for the month of {usersMonth} is: {birthStones[usersMonth]}!")
    # The user also has the option to quit the program using Q which just ends the program with output of goodbye
    elif (usersMonth == "Q"):
        print(f"Goodbye !")
    # finally the else is if the users input was not found in the dictionary AND it was not to quit, will tell them they were wrong and..
    else:
        print(f"{usersMonth} is not the correct input!! Try again ")
        # ...finally will run the function again so that you dont have to run the python file every time you want to test out the program!
        askUser()

# here we call the function for the first time which initiates the users input !
askUser()




### Problem 3
## This problem covers the concepts of:
##      
##      1.Function definition
##      2.Passing and returning variables to and from functions
##      3.Iteration 
##      5.Eroor handling - Breaking out of a program
##      6.formatting output using print

### Create code which:

##  1. contains a function called toCelcius()
##      A. accepts a single variable into the function
##      B. converts the variable to degrees Celcius
##      C. returns the variable to the main program

##  2. contains a function called toFarenheit()
##      A. accepts a single variable into the function
##      B. converts the variable to degrees Farenheit
##      C. returns the variable to the main program


##  3. The main program 
##      A. Asks a user if they want to convert to Farenheit to Celcius select 1, select 2 for Celcius to Farenheit or select 3 to quit
##      B.  Check to make sure the user's reponse is either 1 , 2 or 3, anything else is an invalid choice      
##      B. Depending on the users input of which conversion or quit the program:
##          1. Asks for input of temperature - decimal number
##          2. call the appropriate function and return the answer to the main program.. Print statements are not allowed in the functions.        
##      C. In the main prgram, print out the result of the conversion in an user-friendly answer
##  

## The Formulas
##  1. Celsius to Fahrenheit Formula
#   𝐹 = (𝐶 ∗ 9/5) + 32

##  2. Farenheit to Celcius Formula
#   C=(F - 32) / (9/5)

""" Expected Output
User selects choice 1
Please choose the conversion: 
Enter 1 for Farenheit to Celcius conversion
Enter 2 for Celcius to Farenheit Conversion
Enter 3 to quit 1
please enter a temperature in Farenheit to see the Farenheit Celcius conversion: 212
212.0 Farenheit is 100.00 degrees Celcius 

User selects choice 2
Please choose the conversion: 
Enter 1 for Farenheit to Celcius conversion
Enter 2 for Celcius to Farenheit Conversion
Enter 3 to quit 2
please enter a temperature in Celcius to see the Celcius to Farenheit Celcius: 100
100.0 Celcius is 212.00 degrees Farenheit

User selects choice 3
Please choose the conversion: 
Enter 1 for Farenheit to Celcius conversion
Enter 2 for Celcius to Farenheit Conversion
Enter 3 to quit 3
Thanks for using this program. Have a nice day

User selects choice 4
Please choose the conversion: 
Enter 1 for Farenheit to Celcius conversion
Enter 2 for Celcius to Farenheit Conversion
Enter 3 to quit 4
Invalid choice selected

"""
##  1. contains a function called toCelcius()
##      A. accepts a single variable into the function (Done: Temperatur to convert)
##      B. converts the variable to degrees Celcius (Done: defined by variable inCelcius)
##      C. returns the variable to the main program ( Done: returns inCelcius)

##  2. Farenheit to Celcius Formula
#   C=(F - 32) / (9/5)

def fahrenheitToCelcius(temperatureToConvert):
    inCelcius = (temperatureToConvert - 32) / (9/5)
    return inCelcius

##  2. contains a function called toFarenheit()
##      A. accepts a single variable into the function (DONE: Temperatur to convert)
##      B. converts the variable to degrees Farenheit (DONE: defined by variable inFahrenheit)
##      C. returns the variable to the main program (DONE: returns inFahrenheit)

##  1. Celsius to Fahrenheit Formula
#   𝐹 = (𝐶 ∗ 9/5) + 32
def celciusToFahrenheit(temperatureToConvert):
    inFahrenheit = (temperatureToConvert * 9/5) + 32
    return inFahrenheit

#  3. The main program 
##      A. Asks a user if they want to convert to Farenheit to Celcius select 1, select 2 for Celcius to Farenheit or select 3 to quit
##      B.  Check to make sure the user's reponse is either 1 , 2 or 3, anything else is an invalid choice      
##      B. Depending on the users input of which conversion or quit the program:
##          1. Asks for input of temperature - decimal number
##          2. call the appropriate function and return the answer to the main program.. 

# **************************************

# I DID NOT SEE THIS COMMENT UNTIL I WAS ALREADY DONE WITH THE CODE UNFORTUNATLEY....:
# Print statements are not allowed in the functions.        

# **************************************

##      C. In the main prgram, print out the result of the conversion in an user-friendly answer
##  

# define the function:
def convertTemp(usersChoice):
    usersChoice = usersChoice
    # allow user choice between 1-2-3 (will be converted to an INT)
    try:
        # if user chooses 3, we simply print goodbye and program ends
        if (usersChoice == 3):
            print("Goodbye!")
        # if user chooses 2
        elif (usersChoice == 2):
            # Created Try Exception Blocks in order to stop the user from being able to type in whatever they want, informing them they MUST type in a number
            try:
                # ask user for the tempature to convert (will be a float because tempatures can vary)
                usersTemp = float(input("Enter a tempature for conversion into celcius "))     
                # will create new variable named tempInF which stores the users temp calculated into celcius through passing it in the parameter of my function from earlier (will be rounded up on account of floating input)
                tempInC = round(fahrenheitToCelcius(usersTemp))
                # finally will print out the users original temp and its conversion into Fahrenheit
                print(f"{usersTemp} converted to celcius is: {tempInC}")
            except ValueError:
                print(f"*****Thats not correct ...Must Enter a NUMBER*****")
                convertTemp(usersChoice)

        # DOING THE SAME LOGIC AS COMMENTS FROM ABOVE, FOLLOWING SAME CHAIN OF LOGIC BUT NOW WE ARE DEALING WITH CONVERTING F to C
        elif (usersChoice == 1):
            # Created Try Exception Blocks in order to stop the user from being able to type in whatever they want, informing them they MUST type in a number
            try:
                # ask user for the tempature to convert (will be a float because tempatures can vary)
                usersTemp = float(input("Enter a tempature for conversion into Fahrenheit "))     
                # will create new variable named tempInF which stores the users temp calculated into celcius through passing it in the parameter of my function from earlier (will be rounded up on account of floating input)
                tempInF = round(celciusToFahrenheit(usersTemp))
                # finally will print out the users original temp and its conversion into Fahrenheit
                print(f"{usersTemp} converted to Fahrenheit is: {tempInF}")
            except ValueError:
                print(f"*****Thats not correct ...Must Enter a NUMBER*****")
                convertTemp(usersChoice)
        else:
            print(f"{usersChoice} was not an option ! Try Again!")
            # sends them back to main program (start over)
            mainProgram()
    except ValueError:
        print(f"That is not correct! ...Must Enter a NUMBER")
        # if the error was a value related error, they again are reset with a different message
        mainProgram(usersChoice)

def mainProgram():
    # will try to get users input based on what he wants to convert using:
    try:
        usersChoice = int(input("Enter Number 1 For: Celcius to Farenheit conversion \nEnter Number 2 For: Farenheit to Celcius Conversion \nEnter Number 3 to QUIT! \n"))
        # if the input is valid it will send the users input into the convertTemp Function where the parameters will be replaced with the users input
        convertTemp(usersChoice)
    except ValueError:
        # if the users input is not valid, they get a message and the function re runs in order to get the correct input
        print("Must enter 1, 2, or 3")
        mainProgram()

# CALL FUNCTION FOR FIRST TIME:
mainProgram()

# EXTRA CREDIT: (didnt really understand what it wanted me to do this is my shot at it)
tuple = ("Fahrenheit", "Celcius")
print(f"\n{tuple[0]} : {tuple[-1]}")
## Extra credit is given by only using f-string printing and formatting the temperature output. referencing a a Tuple in the print statements to display the two temperature words (Farenhiet Celcius). 