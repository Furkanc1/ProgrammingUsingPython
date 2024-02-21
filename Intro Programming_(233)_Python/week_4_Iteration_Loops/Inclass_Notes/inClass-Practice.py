# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:24:30 2022

@author: john
"""
############Challenge 1 #########
# suppose you wanted to add a sequence of numbers together and get a sum.
# the sequence is made of contiguous numbers,
# write code to sum a sequnce of numbers.  Ask a user a starting number and how
#many consecutive numbers to sum together
## HINT: Initialize a variable to hold the total by first assigning the 
#variable to 0. Then do your math and assign the total to it. 

""" Expected Output
What is your starting number? 1
How many numbers in the sequence? 10
The sum of nmbers from 1 to 10 is 55

# """

# RANGE HAS 3 PARAMETERS (STARTING VALUE, STOPPING VALUE, STEPPING VALUE(skipping))
startingNumber = int(input("What is your starting number?"))
numbersInSequence = int(input("How many numbers in the sequence?"))

sumOfNumbers = 0

for numbersInTheRangeOfTheFollowing in range(startingNumber, numbersInSequence + 1):
    sumOfNumbers = sumOfNumbers+numbersInTheRangeOfTheFollowing

print(f"the sum of numbers from {startingNumber} to {numbersInSequence} is {sumOfNumbers}")

############Challenge 2 #########

#Suppose you have a list of cars named cars. 
# Write a short piece of code using a for loop to print out the entire list
  
""" Expected output
Ford
Chevrolet
Dodge
Range Rover
BMW
Mercedes
Toyota
Nissan
Kia
"""

###########Challenge 2 Code Below ########################
    
cars=["Ford", "Chevrolet", "Dodge", "Range Rover", "BMW", "Mercedes", "Toyota", "Nissan", "Kia"]
for x in cars:
    print(f"Here is the list of ALL cars: {x}")
    
    
    
    
############Challenge 3 #########    
# Once you get the loop to print out the entire list, the challenge is to
#start with the first car manufacturer in the list and print out every other 
# manufacturer    
#HINT: use the range() function to help you    
""" expected Output

Ford
Dodge
BMW
Toyota
Kia
"""
# Heres the list
cars=["Ford", "Chevrolet", "Dodge", "Range Rover", "BMW", "Mercedes", "Toyota", "Nissan", "Kia"]
# cars[0:8:2] (SIMILAR TO THIS)

for x in range(0, len(cars), 2):
    print(f"Here is every other car: {cars[x]}")
    

############Challenge 4 #########    
#Now use the same code as challenge 3 and start from the second manufacturer
# and print out every other manufacturer
    
""" expected output
Chevrolet
Range Rover
Mercedes
Nissan
"""

for x in range(1, len(cars), 2):
    print(f"Here is every other car starting with second car: {cars[x]}")
    
############Challenge 5 #########  

# using a for loop, print out a set of even numbers from 0 to 20, then reuse the code to print a set of odd nbumbers from 0 to 20

"""Expected Output - Even
2
4
6
8
10
12
14
16
18
20

Expected Output Odd
1
3
5
7
9
11
13
15
17
19

"""

for evenNumber in range(2, 21, 2):
    print(f"Here are EVEN Numbers: {evenNumber}")

for oddNumber in range(1, 21, 2):
    print(f"Here are ODD Numbers: {oddNumber}")
