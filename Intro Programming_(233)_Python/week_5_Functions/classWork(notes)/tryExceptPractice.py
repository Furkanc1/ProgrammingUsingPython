# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:06:00 2022

@author: johnk
"""

## Class project

#We are creating a guessing game in class.
## the game play as follows
"""
1. player 1 enters a wholeuser number. THis is the secret number that player 2 will guess
    a. the number must be a whole number and if it is not, we have to catch the error , print out a 
    user friendly message and start the program again
2.  player 2 will be asked to enter a whole number or type 'q' to quit
    a. the number must be a whole number and if not the user gets a friendly message to select a 
    new number
    b. if q is selected, then a funny message appears and the person is given the secret number
    
    
#### Expected Output
    
Player 1, please enter the secret number hello
You entered a value which is not a valid whole number.

Player 1, please enter the secret number 22.3
You entered a value which is not a valid whole number.

Player 1, please enter the secret number 25

Player 2, please enter a whole number or q to quit: 23.3
You entered a value which is not a valid whole number.

Player 2, please enter a whole number or q to quit: hi
You entered a value which is not a valid whole number.

Player 2, please enter a whole number or q to quit: 25
You guessed it. The secret number was 25

Player 2, please enter a whole number or q to quit: q
Couldn't guess huh? The secret number was 25

"""
