# import circleCLass from circle
from circkeClassHw import Circle

# create empty list to store users data
listOfData = []

# function which asks user their radius
def askUser():

    # variable for their input (radius)
    userRadius = (input("Please input a radius of a circle in feet or q to quit: ")).lower()

    # if they want to quit we just print goodbye! and show them their results
    if (userRadius == "q" or userRadius == "quit"):
        print("Goodbye!")

        # function for printing their search results
        storedValues(listOfData)

    # else we start a try-except block
    else:

        # will TRY this, taking users input and converting it into a float, if it works then we send to the calculate function
        try:
            radiusAsFloat = float(userRadius)
            calculate(radiusAsFloat)
        
        # Except, if there is a value error, meaning the input couldnt be converted into a float, user will have to try again
        except ValueError:
            print(f"{userRadius} was not valid, Try Again!")

            # send back to beginning of the function if their input was nt valid
            askUser()
            
# Calculating the data function, here is where we send the users radius to the other file for calculating,
def calculate(radius):
    # sending radius to self
    circleData = Circle(radius)

    # using self.radius to find the following info:
    # area circumference and diameter
    area = circleData.findArea()
    circumference = circleData.findCircumference()
    diameter = circleData.findDiameter()

    # PRINT out the results so the user can see the data
    print(f"Your circle radius is {radius}\nYour circle area is {area} ft.\nYour circle diameter is {diameter} ft.\nyour circle circumference is {circumference} ft.")

    # Append the results we get from the returns in the other file to the empty list 
    # (we append it as a tuple so that EACH indivisual tuple is basically its own circle)
    # this part is important because the order of these elements is how we will access it later in the stored values function
    listOfData.append((radius, area, diameter, circumference))

    # then send to askAgain function which will Literally ask if htey want another circle's data or not
    askAgain()

# ask again function:
def askAgain():
    # asks user if they want another circles data
    userInput = input(F"Would you like to find another circle? Yes (y) or No (n)").lower()

    # if not, they are told goodbye and their stored values
    if (userInput == "n" or userInput == "no"):
        print(f"Goobye!\n\n")

        # function for printing the stored values
        storedValues(listOfData)

    # Else if, the user puts yes, then we just ask them again waht their radius is by sending them back to askUser Function
    elif (userInput == "y" or userInput == "yes"):

        # askUser function:
        askUser()

    # else: if their input was not yes or no, then they are sent to beginning of this function (askAgain)
    else:
        print(f"{userInput} was not valid, type Yes (y) or No (n)")
        askAgain()

# Printing stored values function: (takes in empty list which was appended to in previous functions)
def storedValues(list):

    # looping through the length of the list allowing us to access each elemtn in it
    print("\n\nYour Stored Values Were:\n\n")
    for x in range(len(list)):

        # here is were we define indivisual tuples in the list as data:
        Data = list[x]

        # Now we take the values in the tuple (which are all floats) and assign them to values (MUST BE SAME ORDER THAT IT WAS APPENDED AS)
        (radius, diameter, area, circumference) = Data
        
        # Print statement to finally show the Radius and the corresponding data values for that Circle(radius)
        print(f"Radius: {radius}\n -Area : {area} ft.\n -Diameter: {diameter} ft.\n -Circumference : {circumference} ft.")

# Here is where we start running the program when the file is run!
askUser()
