# Course: Introduction to Programming (INFO-233)
# Student Name: Furkan Coskun

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

#########################
# Problem 1: Hello World!
#########################

"""This problem is to ensure that you are properly set up with a Python
# programming environment. After opening your environment

# Create a print statment to print Two words together as one line using two separate arguments in one print statment
 
# After your programe runs, recreate this program , but now print "Hello World!" one letter at a time separated by three
#dots bewteen each letter so your output will look like the sample below

#  Sample output - output should not have the "#" 
#########################
Hello World!
H...e...l...l...o... ...W...o...r...l...d...! 

######################### """

#########################
# HINT: research the sep parameter in print()
#########################

# Print will print out similar to console.log, sep="" function will seperate everything inside the print() by the value assigned
# can this be enhanced with a sort of for loop{} to loop through every letter in the sentence hello world, and then seperate it?

# REUBSMITTION COMMENT: Sepererated everything into variables
# same logic but now it follows the instruction above
hello = "Hello"
world = "World"
character = "!"
print(hello, world, character)

h = "H"
e = "e"
l = "l"
o = "o"
w = "W"
r = "r"
d = "d"
space = ""

print(h,e,l,l,o,space,w,o,r,l,d,character, sep="...")


# FOR LOOP VERSION ( I LOOKED IT UP SOURCE: https://www.w3schools.com/python/python_for_loops.asp, https://www.geeksforgeeks.org/python-sep-parameter-print/ )
# UPDATE DID NOT WORK NOT SURE WHY IT WONT SEPERATE THE ARRAY 
# usersInputForSeperation = input("enter text for seperation")

# for x in usersInputForSeperation:
#     print(x, sep = "-")



#########################
# #Problem 2: working with Variables and math
#########################

""" This problem will look at using variables to represent the value. you will assign values to variables
and perform some simple math to get an answer

(How many times should we stop to for fuel along the way ?) 

Given the total miles for the trip is  1,044.5 mi. Our car gets pretty crappy mileage on the highway so let's assume we get 22 mpg
and our gas tank can hold 18 Gallons.  """

# Constraints
""" 
1.  Your formula to calculate the answer should only perform math on variables, numbers in the formula
cannot be used.
2.  Your final answer must be a whole number since you cannot stop for a fraction. 
3. You must include comments in  your code to explain the math involved. 
"""  # #HINT: Research the round()

# RESUBMITTION COMMENT: Created third variable for GallonsPerCar, I must have overlooked this part cause until i saw the comment i did not realize that taking 20 stops while only going like 1000 miles made NO sense lol, Now it will do the same logic but take into account the (GALLONS * MILESPERGALLON)

# total trip turned into variable
tripTotalMileage = 1044.5
# car mileage per gallon turned into variable
milesPerGallon = 22
gallonsInCar = 18

# (RESUBMITTION) --> NEW VARIABLE:
travelLimitForSetCar = milesPerGallon * gallonsInCar 
# FIRST COMMENT BEFORE I USED ROUND: create a new variable representing the amount of stops to take, then its just math, 1044.5 divided by 22, and use // as the smybol in order to not get a decimal.

# NEW COMMENT: Round makes this easier because i dont have to do the // and have the console log 47.0 rather than 47
stopsToTake = round(tripTotalMileage / travelLimitForSetCar)

print("PROBLEM 2 ANSWER_1: Take", stopsToTake, "stops.")

""" For the second part of this problem set, we want to explore using different vehicleswith different MPG - modify the problem to ask
the user the MPG of the vechicle 
"""

# Constraints
""" 
1.  Your formula to calculate the answer should only perform math on variables, numbers in the formula
cannot be used.
2.  Your final answer must be a whole number since you cannot stop for a fraction. 
3. You must include comments in  your code to explain the math involved. 
"""

#########################
# HINT - Use you knowledge of round() and also research the use of input()
#########################

# total trip turned into variable
tripTotalMileage = 1044.5
# car mileage per gallon turned into user input variable, int promises it will return integer, rather than the string the the input() function returns normally
# UPDATE ON COMMENT ABOVE: Int did not end up working when i did it like this : input(int("text")),, but when deconstructed it worked fine

# RESUBMITTION COMMENT: Same logic as above, but this time taking in the Users Variable for their Miles Per gallon as well as total Gallons their car carries ( Could also enhance by creating a third input being how far the user wants to travel? i think ill add that now actually)

usersMilesPerGallon = input("What is your cars MilesPerGallon ")
usersTotalGallons = input("How many gallons does your car hold?")
UserTripDistanceInMiles = float(input("How far are you travelling (IN MILES)? "))

usersMilesPerGallonAsInt = int(usersMilesPerGallon)
usersTotalGallonsAsInt= int(usersTotalGallons)

TravelLimitForUsersCar = (usersMilesPerGallonAsInt * usersMilesPerGallonAsInt)

# NEW COMMENT: Round makes this easier because i dont have to do the // and have the console log 47.0 rather than 47
stopsToTake = round(UserTripDistanceInMiles / TravelLimitForUsersCar)

print("You should take", stopsToTake, "stops on this trip based on provided information.")