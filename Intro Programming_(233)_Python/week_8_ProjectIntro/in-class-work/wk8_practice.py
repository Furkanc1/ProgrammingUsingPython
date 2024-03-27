# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 08:25:35 2022
@author: john
"""
## Coding challenge 1##
## Create a program which simulates a dice roll with two die using hte random module
## each die has the numbers from 1 to 6
## The expected output below shows what should print out for each roll of the dice
## Notice the difference when I roll 8? You must incorporate logic to change the output statement 
## when an 8 is rolled

## Hint ##
## Lookup the Random module from the link on the notes page, and research random.choice(seq).  The seq is a list of numbers for a single die. 

""" Expected output
you rolled a 10, Die1 was 4, Die2 was 6
you rolled an 8, Die1 was 2, Die2 was 6
"""
### Code goes below ###
# create a list of numbers 1-6
diceList = [1, 2, 3, 4, 5, 6]

import random;
def randomChoice():
    # die 1 = a random choice from the list above (1-6)
    die1 = random.choice(diceList)
    # die 2 = a random choice from the list above (1-6)
    die2 = random.choice(diceList)
    # your roll again = total between the two dies
    yourRoll = (die1 + die2)
    # print results
    print(f"Your rolled: {yourRoll}, \nFirst Die: {die1} Second Die: {die2} ")
    # print(f"First Die: {die1} \nSecond Die: {die2}")
# call function to run initially
randomChoice()


## Coding challenge 2##

#Review the documentation top use yfinance
##    https://pypi.org/project/yfinance/

## We are going to query Yahoo finance for data on stocks.
## In order to use this module in Anaconda, you must first install it. Using a 
## terminal in Anaconda, enter the phrase below without the #

# conda install -c conda-forge yfinance


# Once Installed, import the yfinance package.
# Get input on a ticker symbol from user
# set the input as the ticker symbol for yfinance using the .Ticker method and assign it to a varible
# You should be able to print the varible.info and receive a dictionary of ticker items

### Code goes below ###

# from board:
import yfinance as yf;
myinput = input("please entera stock symbol: ")
mystock=yf.Ticker(myinput)
information = mystock.fast_info

print(information)
