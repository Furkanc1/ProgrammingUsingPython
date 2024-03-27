# We are going to use the random module to simulate rolling a pair of dice.  There are two methods to random we are going to use:

# random.randrange()
# random.choice
# Using  random.randrange()

# Import the random module
# using two variables (one for each die)
# Use  random.randrange() to simulate rolling a pair of dice
# Display each die roll result and add the results to display the total
# for example , if the first die rolls 1 and the second die rolls a 6, the total of the pair is 7

# Next use Random.choice()

#  import the random package
# create a list containing each number which represents a side of a die
# using random.choice() randomly roll each die 
# Display each die roll result and add the results to display the tot
# upload the code here as die_roll_yourlastname.py

# importing Random
import random; 
# setting each die to a range between 1-6 (stop at 7 because of the stop property)
diceOne = random.randrange(1,7)
diceTwo = random.randrange(1,7)

# creating roll dice function
def rollDice():
    # your roll = total number from two dies
    yourRoll = (diceOne + diceTwo)
    # print out the value dice1 and dice 2 landed on and print the total of the two
    print(f"First Die: {diceOne} \nSecond Die: {diceTwo}")
    print(f"Your rolled: {yourRoll} ")
# run the function
rollDice()
# create a list of numbers 1-6
diceList = [1, 2, 3, 4, 5, 6]

# define function 
def randomChoice():
    # die 1 = a random choice from the list above (1-6)
    die1 = random.choice(diceList)
    # die 2 = a random choice from the list above (1-6)
    die2 = random.choice(diceList)
    # your roll again = total between the two dies
    yourRoll = (die1 + die2)
    # print results
    print(f"First Die: {die1} \nSecond Die: {die2}")
    print(f"Your rolled: {yourRoll} ")
# call function to run initially
randomChoice()

# Another way to do it using for loop + Range
diecount = 0
dieList2 = [1,2,3,4,5,6]
for die in range(1,3):
    myDie = random.choice(dieList2)
    print(f"Die {die} rolled {myDie}")
    diecount = diecount + myDie
print(f"total roll: {diecount}")

from random import seed, randrange

def rollDie():
    die = randrange(1,7)
    return die

