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
# Dictionary of terms (in this case rock and its abilities, Paper and its abilities and Paper + its abilities) (i opted for the easier representation of rock paper and scissors because who really wants to sit there and type the ENTIRE word when one character will do.)

# IMPORTING random from python ( similar to imports using NODE.js (npm) ) basically is just math.random() but has to be imported to be used first
import random

# defining the Logic for how the game is won:

# two parameters in gameWinnerLogic can be named anything as they are my own variables. They represent the UsersChoice from the INPUT() as well as the randomly generated AIChoice from the AutomatedCHoiceLogic()
def playAgainLogic():
    playAgainPrompt = input("Would you like to play again?? ( y ) or ( n ) : ").lower()
    if (playAgainPrompt == "y" or playAgainPrompt == "yes"):
        startGame()
    elif (playAgainPrompt == "n" or playAgainPrompt == "no"):
        print("Goodbye! Thanks for playing :) ")
    else:
        print(f"{playAgainPrompt} was not an option, Please select Yes(y) OR No(n). Thank You! ")
        playAgainLogic()

def gameWinnerLogic(theUsersChoice, theRobotsChoice):
    # if the both choices == one another,
    if (theUsersChoice == "r" and theRobotsChoice == "Rock") or (theUsersChoice == "p" and theRobotsChoice == "Paper") or (theUsersChoice == "s" and theRobotsChoice == "Scissors"):
        print("TIE GAME !!!")
        playAgainLogic()
    elif (theUsersChoice == "r" and theRobotsChoice == "Scissors") or (theUsersChoice == "s" and theRobotsChoice == "Paper") or (theUsersChoice == "p" and theRobotsChoice == "Rock"):
        print("You WIN !!! ")
        playAgainLogic()
    else:
        print("You LOSE !!! ")
        playAgainLogic()

def automatedChoiceLogic():
    choices = ("Rock", "Paper", "Scissors")
    randomChoice = random.choice(choices)
    return randomChoice

choicesDictionary = {
    "r": "The rock is able to break the scissors, but can be defeated by the paper",
    "p": "The paper is able to wrap the rock up, but is easily cut by the scissor",
    "s": "The scissor is able to cut paper, but is smashed by the rock",
}

def startGame():
    choices = ("r", "p", "s")
    userChoice = input("Please Choose: Rock=(r), Paper=(p), Scissors=(s) or Quit=(q) : ").lower()

    if userChoice in choices:
        robotChoice = automatedChoiceLogic()
        print(f"The automated opponent chose: {robotChoice} ")

        gameWinnerLogic(userChoice, robotChoice)

    elif userChoice == "q":
        print("Goodbye! Thanks for playing")
    else:
        print(f"{userChoice} is NOT a valid choice. Try again with (r), (p), (s), or (q) to quit.")
        startGame()

startGame()


