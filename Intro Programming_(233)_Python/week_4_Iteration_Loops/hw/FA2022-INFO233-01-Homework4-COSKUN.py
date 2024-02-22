# Course: Introduction to Programming (INFO-233)
# Student Name: 

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

##############
# Problem 1
##############

# Create a list of values from 0 to 300 (including 300) in incremenets of 3 (0, 3, 6...).
# Iterate through every value, and confirm whether the value is even or odd.
# Do you notice anything interesting?
##HINT Create an empty list. Research .append() method. Iterate through a range of numbers 
#as specified and append the values to the list. iterate through the new list and test each value 
# for odd and even
 
""" Expected Output
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78,
 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144,
 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207,
 210, 213, 216, 219, 222, 225, 228, 231, 234, 237, 240, 243, 246, 249, 252, 255, 258, 261, 264, 267, 270,
 273, 276, 279, 282, 285, 288, 291, 294, 297, 300]

0 is even
3 is odd
6 is even
9 is odd
.
.
.
300 is even
"""
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t PROBLEM 1")
# First we have to create the list of numbers using the Range() function
listOfNumbers = range(0, 301, 3)
for x in listOfNumbers:
    print(x)
# Expected output: 0 3 6 9 12 15 ..... 300

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t PROBLEM 1 PART 2")
# next create a for loop so that i can loop through all the values in my list (or range) and run them through an if-statement nested in the for loop
for number in listOfNumbers:
    # will check first if "number" % 2 == 0... The % is "modulo opertator" and its power is basically to return the remainders for whatever numbers are divided. (EX: 2/2 = 1, Therefore there is NO remainder, but 3/2 = 1.5 Therefore there is ALWAYS a remainder (IN THIS CASE, 0.5)...)
    # This first if condition checks to see if the number (value in the list) is divisble by 2 with NO REMAINDER... If that is the case, then the number must be even
    if (number % 2 == 0):
        print(f"{number} is an EVEN number")
    else:
        # ELSE, meaning if "number" is divisble by 2 but has a remainder of ANYTHING, that means that number is ODD and welog that below
        print(f"{number} is an ODD number")

##############
# Problem 2
##############
# Tuition increases are common. Our tuition is currently $8000 a year. 
#With an expected increase of 3% a year for the next 5 years, write code to calculate
# the tuition for each year for 5 consecutive years.  
#Write the code twice, once with for loop and once with a while loop

""" Expected Output
Tution will increase from the current amount of: $8,000.00 as follows: 

Year 	 New Tuition
---- 	 -----------
2023 	 $8,240.00
2024 	 $8,487.20
2025 	 $8,741.82
2026 	 $9,004.07
2027 	 $9,274.19
"""
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t PROBLEM 2")


# FOR LOOP:
print("*****************************\t FOR-LOOP (BELOW)")

# first create the variables which will represent the static information provided above
currentTuition = 8000
# rate of increase is 3% which is really 3/100 which is really 0.03
percentRateOfIncrease = 0.03
# This represents the range of years we are trying to find, i made this into a variable so in future cases i can just change the range and the current year so that i wont have to ever touch these lines of code again (just change the variable to suit my needs)
rangeOfYearsToIncrementBy = 5
currentYear = 2023
# https://www.guru99.com/python-escape-characters.html#:~:text=%E2%80%9C%5Ct%E2%80%9D%20allows%20inserting%20a,new%20line%20between%20python%20strings.
# Here is where the headers in the terminal are created, using the \t escape sequence ^^^ more on this on website above (basically \t will create a space between the print statement used for no other reason other than better formatting in terminal)
print(f"Year\t Expected Tuition")
print(f"----\t ----------------")

# for loop which basically takes "theYear" which is my variable representing each value in the range
# Range(currentYear, currentyear + rangeOfYearsto increment) which means that the range is from "currentYear" or 2023, to "currentYear" or 2023 PLUS the range of years i want to look into the future by (IN THIS CASE 5) which will basically return:
# 2023, 2024, 2025, 2026, 2027 (AKA THE NEXT 5 YEARS) which is represented by my variable "theYear"
for theYear in range(currentYear, currentYear + rangeOfYearsToIncrementBy):
    # Next we have to redefine the currentTuition, because if we just print current tuition it wont go up at all.
    # We redefine it as CurrentTuition *= (explenation of *=: *= is an operator similar to == or != which basically says that the "currentTuition" TIMES (*) whatever is after the *= will REDEFINE the variable "currentTuiition" as the value that is returned)
    # Explenation using problem: CurrentTuition *= (1 + Rate) IS THE SAME AS --> tuitionCurrentValue(8000) TIMES (1.3) IS EQUAL TO tuitionsNewCurrentValue (this is all done in the backround and changing the variable name is not necessary)
    currentTuition *= (1 + percentRateOfIncrease)
    # Finally if we just print current tuition it will eventually give us a BUNCH of decimals and we get rid of this issue simply by rounding up by 2 decimal places as it shows in the expected output
    # currentTuitionRoundedUp = round(currentTuition, 2)
    # similar to print statements above, seperate the two variables with a space by using the \t "ESCAPE SEQUENCE" which is how the expected output seems to be done
    # DONT EVEN NEED TO DO ROUND UP ANYMORE AS .2f TAKES CARE OF THE DECIMALS (EXPLAINED BELOW IN FOR-LOOPS (thats where it was discovered))
    print(f"{theYear}\t ${currentTuition:.2f}")

# BASICALLY: For every value in the range of Current year(2023) THROUGH (2023) + 5 (aka 2027), run the current tuition(8,000$) through the equation which will redefine the tuition, and PRINT IT OUT(round up 2 by using formatter)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t PROBLEM 2 PART 2")


print("*****************************\t WHILE-LOOP (BELOW)")
# WHILE LOOP (meh):
# basically the same logic but now we are starting from the last year and working down toward the current year
    # copy and pasted print statments from for-loop above
print(f"Year\t Expected Tuition")
print(f"----\t ----------------")

# SAME LOGIC AS FOR LOOP (created new variables because it just continued where the for loop left off)
endingYear = 2027
currentYear2 = 2023
currentTuition2 = 8000
# LOGIC: So while the current year(2023) is LESS THAN OR EQUAL TO ending year(2027): 
while currentYear2 <= endingYear:
    # Take the current tuition and multiply it by 1 + 0.3(rate of increase) and reassign current tuition2 to that output for every value of current year THROUGH ending year
    currentTuition2 *= (1 + percentRateOfIncrease)
    # ROUND UP 2 DECIMAL PLACES
    # currentTuitionRoundedUp = round(currentTuition2, 2)
    # WE ENDED UP NOT EVEN NEEDNIG TO ROUND UP AS THERES A MORE EFFICIENT WAY :below  
    # Adding to the end of the variable inside a print statment :.2f is a "FORMAT SPECIFIER" which will take the FLOAT NUMGER and after the "." will only allow 2 more numbers as specified to be printed 
    # source: https://www.quora.com/What-is-2f-in-Python 
    print(f"{currentYear2}\t ${currentTuition2:.2f}")
    # MAKE SURE TO ADD 1 and REDEFINE CURRENT YEAR EVERYTIME LOOP RUNS OR IT WILL RUN FOREVER BECAUSE 2023 WILL ALWAYS BE LESS THAN 2027
    currentYear2 += 1

# Basically: While the current year is still less than the year we want to stop at run the tuition equation, and print the year that it is and its CORRESPONDING tuition (round 2 decimal places using formatter) AND DONT FORGET TO INCREMENT THE YEAR BY 1 OR IT WILL RUN FOREVER BECAUSE 2023 is ALWAYS ALWAYS ALWAYS less than 2027, unless you add 1 to it every time the loop runs (2023 +1, 2024+1, 2025+1, 2026+1...etc)

############
# Problem 3
##############

# Write code to display a table of Celsius temps from 0 to 20 and its Fahrenheit equivalent

# HINT## Use a loop and iterate through a range of numbers as specified above. Research how to add tabs in a print statement
#Research formatting to two decimal places with print. 
## formula to convert Farenheit to Celsius °F = (°C × 9/5) + 32
""" Expected Output
Celsius 	 Fahrenheit
------- 	 ----------
0 	 	 	 32.00
1 	 	 	 33.80
2 	 	 	 35.60
3 	 	 	 37.40
4 	 	 	 39.20
5 	 	 	 41.00
6 	 	 	 42.80
7 	 	 	 44.60
8 	 	 	 46.40
9 	 	 	 48.20
10 	 	 	 50.00
11 	 	 	 51.80
12 	 	 	 53.60
13 	 	 	 55.40
14 	 	 	 57.20
15 	 	 	 59.00
16 	 	 	 60.80
17 	 	 	 62.60
18 	 	 	 64.40
19 	 	 	 66.20
20 	 	 	 68.00
"""
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t PROBLEM 3")

# PRINT HEADERS (explained above in For-Loop)
print("Celcius\t Fahrenheit")
print("-------\t ----------")
# Create Range (explained in For-Loop)
celciusRange = range(0, 21)

# for celcius(Variable which represents every number in range of 0-20) inside the range of 0-20:
for celcius in celciusRange:
    # created new variable which is just converting celcius ot Fahrenhiet which is the equation given above:
    fahrenheit = (celcius * 9/5) + 32
    # Now we print out the celcius value (TAB or SPACE) then we print out the fahrenheight value and ROUND 2 DECIMAL PLACES using the "FORMAT SPECIFIER" (explained in While-Loop)
    print(f"{celcius}\t {fahrenheit:.2f}")

# Basically for every value in range (0-20) it will take that value, run it through the equation and be represented by the fahrenheit variable
    # THEN when we log it, we first log the celcius (0-20) on the left, then TAB or SPACE and log every CORRESPONDING Fahrenheit value on the right and round 2 decimal places

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t FIN.")
# if you couldnt tell i like this seperator thing its pretty good for formatting purposes
