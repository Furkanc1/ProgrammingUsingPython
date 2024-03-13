"""
Welcome to the proactice coding portion of the Mideterm for INFO-233

Directions: -  Credit for the problem will not be given without proper comments. All code must contain comments to explain your logic.
    
    1. Read through all of the comments in this file and follow the directions exactly. 
    2. Your code's output must match the expected output from each problem.
    3. Original work only. Your work must be your own. 
    4. When completed, save the file as info-233-midterm_practice _yourlastname and uipload it the assignment in Canvas
    5. Good luck and relax. Use all of the resources you have. 
"""

############################################################ Problem 1  ############################################################################################
## This problem covers the concepts of:
##      1. dictionaries
##      2. iteration using for loops
##      
## Given the dictionary below, 
##      1.append the key 'New York City Queens' and the value 'New York Mets',
##      2. Print out the contents of the ditcionary one key:value pair per row
##      4. Display all of the cities  contained in the dictionary to the screen one item per row  and ask a user to choose one city to delete and delete the dictionary entry
##      5. Test the dictionary to see if the delete was successful 

mlbTeams = {
    'Baltimore': 'Baltimore Orioles', 
    'Boston': 'Boston Red Sox', 
    'New York City Bronx': 'New York Yankees', 
    'St. Petersburg': 'Tampa Bay Rays', 
    'Toronto': 'Toronto Blue Jays', 
    'Chicago': 'Chicago Cubs', 
    'Cleveland': 'Cleveland Indians', 
    'Detroit': 'Detroit Tigers', 
    'Kansas City': 'Kansas City Royals', 
    'Minneapolis': 'Minnesota Twins', 
}

    
# 1
mlbTeams.update({"New York City Queens":"New York Mets"})

# 2
print("\nIterate through the keys and values at the same time")
for city in mlbTeams:
    print (city,':',mlbTeams[city])

for city in mlbTeams:
    print(city)

selectedCity = input("Enter a City for deletion ").title()

mlbTeams.pop(selectedCity)
if (selectedCity) in (mlbTeams):
    print("Error Deleting City")
else:
    print(f"*******************************************{selectedCity} was deleted successfully!")
print("************************************************  \nNew Dictionary:")
for city in mlbTeams:
    print(city)







############################################################ Problem 2  ############################################################################################
## This problem convers the concepts of:
##      1. function definition
##      2. Passing variable to and from functions
##      3. fstrings
##      
## Create code which
##  1. Asks a user to input a number
##  2. Take the number and pass it to a function called sqIt()
##  3. Within the function, square the number and return the value to the main program
##  4. Using an fstring, Printout the squared value to the screen as shown in the expected output

""" Expected Output


Please enter a number to square: 23
the numeber you entered was 23, and its square is 529

"""
def SquareIt(usersNumber):
    squareNumber = ( usersNumber ** 2)
    return squareNumber

def askUser():
    try:
        userInput = round(int(input("Enter a Number for squaring: ")), 2)
        finalResult = SquareIt(userInput)
        print(f"The number: {userInput} squared is equal to: {finalResult}!")
    except ValueError:
        print("Must Enter A Whole NUMBER!!")
        askUser()
askUser()