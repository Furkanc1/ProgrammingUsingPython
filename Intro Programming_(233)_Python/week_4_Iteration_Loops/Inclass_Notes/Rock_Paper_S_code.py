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
    # if the both choices == one another, will print that its a tie game and run play again logic to ask user if they want to play again??
    if (theUsersChoice == "r" and theRobotsChoice == "Rock") or (theUsersChoice == "p" and theRobotsChoice == "Paper") or (theUsersChoice == "s" and theRobotsChoice == "Scissors"):
        print("TIE GAME !!!")
        playAgainLogic()
    # elif: the users choice beats the AI's choice logically then will print that you won! ( we control how the logic works in this line because if i wanted to i could make paper beat scissors but the rules of the game would be different then. ) 
    elif (theUsersChoice == "r" and theRobotsChoice == "Scissors") or (theUsersChoice == "s" and theRobotsChoice == "Paper") or (theUsersChoice == "p" and theRobotsChoice == "Rock"):
        print("You WIN !!! ")
        playAgainLogic()
    else:
    # Any other case will result in the user LOSING to the AI because if they dont tie and they dont win, theres only one option left, LOSE and then they are asked if they want to play again!
        print("You LOSE !!! ")
        playAgainLogic()
# This is where the Random Choice is selected by the PROGRAM to play against the users choice
def automatedChoiceLogic():
    choices = ("Rock", "Paper", "Scissors")
    # random choice uses the import Random,  and selects a random index from the given tuple. --> Similar to math.random() where it chooses an index from 0.000 - 0.9999 (or just 1) and based off that chooses one of the options
    randomChoice = random.choice(choices)
    return randomChoice
# defining what each of the choices defeat and are defeated by in a dictionary (basically a json object with key value pairs)
choicesDictionary = {
    "r": "The rock is able to break the scissors, but can be defeated by the paper",
    "p": "The paper is able to wrap the rock up, but is easily cut by the scissor",
    "s": "The scissor is able to cut paper, but is smashed by the rock",
}

# Start game logic, Will ask user for their input from the choices
def startGame():
    choices = ("r", "p", "s")
    # users choice is automatically lowercased for future-logic purposes ( == ) <--- so that is true
    userChoice = input("Please Choose: Rock=(r), Paper=(p), Scissors=(s) or Quit=(q) : ").lower()

    # checks to see if userChoice is in the choices given
    if userChoice in choices:
        print(f"You chose: {userChoice}, {choicesDictionary[userChoice]}")
        # defines the robots choice by running the automated choice logic function above
        robotChoice = automatedChoiceLogic()
        print(f"The automated opponent chose: {robotChoice} ")

        # next it it will run the gameWinnerLogic function which takes in two parameters, the userChoice and RobotChoice... These parameters are also DYNAMICALLY redefined inside the actualy GWL Function using the ROBOTCHOICE(random) AND USER CHOICE(input)
        gameWinnerLogic(userChoice, robotChoice)

    # If the user selected q as their input this will quit the game for them
    elif userChoice == "q":
        print("Goodbye! Thanks for playing")
    # ELSE: if anything else is typed other than R P S or Q then the program will reject it and guide them to either quit or select the correct input for the game to run, and will run the startGame function from the start!
    else:
        print(f"{userChoice} is NOT a valid choice. Try again with (r), (p), (s), or (q) to quit.")
        startGame()

# here is where we call the function to actually start the game once the file is run in the python environment
startGame()


