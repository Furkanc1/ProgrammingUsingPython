# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:01:33 2023

@author: john
"""
""" We are creating the introduction to a rock paper scissors game. In this 
first part, we will introduce the main characters to the player. using the three descriptions provided below,
create a small snippit of code which will 

1. ask a user to choose between rock , paper or scissors
2. Check to see if the playuer's input is either rock, paper or scissor. If it is, execute the next step
if it isn't , let the player know their choice was not rock paper or scissor
2. Display the characteristic of the user item the player chose
'

Rock
The rock is able to break the scissors, but can be defeated by the paper

Paper 
The paper is able to wrap the rock up, but is easily cut by the scissor

Scissor
The scissor is able to cut paper, but is smashed by the rock

"""

### Hint, Use a dictionary to list out the pieces and descriptions
### Create a tuple of the three choices.  Can you figure out why a tuple and not a list?
### Use a conditional and check to see if the input is contained in the tuple, and if it is,
### print out the fact about the choice. If it isn't print out an error message
### use the correct method to ensure the user's choice is searchable in the dictionary
### Finally use f string to print out the statement. 

## Your program should look like the output below if a user selects "Rock". the error message if a person types in 'glue'. All output should be in a consistent format
""" Sample output below

Please choose: Rock, Paper or Scissors: Rock
Here are the characteristics of Rock:
The rock is able to break the scissors, but can be defeated by the paper

Please choose: Rock, Paper or Scissors: glue
Sorry, glue is not one of the valid choices, Please enter ('rock', 'paper', 'scissor')

""" 

# 1. ask a user to choose between rock , paper or scissors
# 2. Check to see if the playuer's input is either rock, paper or scissor. If it is, execute the next step
# if it isn't , let the player know their choice was not rock paper or scissor
# 2. Display the characteristic of the user item the player chose

usersChoice = input("Please Choose: Rock(r), Paper(p), Scissors(s)")