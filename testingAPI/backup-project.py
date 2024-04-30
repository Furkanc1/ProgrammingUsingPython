# requests for getting back information from API requests
import requests

# json used to format dictionary when outputted
import json

# textwrap used to wrap Long lines of text like descriptions
import textwrap

# prerryPrint which prints out results so they are readable
from pprint import pp 

# random used to get a random number for generating random recipe function
import random

# import PIL which basically opens up images from a Url automatically (doesnt work yet need to get running)
from PIL import Image

# **** The Cocktail DB ****

# headers defined (api key and host link)
apiHeader = {
	"X-RapidAPI-Key": "EnterKeyHere_sameKeyForBoth)",
	"X-RapidAPI-Host": "the-cocktail-db3.p.rapidapi.com"
}

# **** Cocktail by API-Ninjas ****

# headers defined (api key and host link)
searchedCocktailHeader = {
    'X-RapidAPI-Key': 'EnterKeyHere_sameKeyForBoth',
    'X-RapidAPI-Host': 'cocktail-by-api-ninjas.p.rapidapi.com',
}

# here we are able to get data back for ALL the drinks available on the api we are using
cocktailsUrl = "https://the-cocktail-db3.p.rapidapi.com/"
response = requests.get(cocktailsUrl, headers = apiHeader)

# response.json parses out the response for all drinks (essentially turning it into a dictionary)
allDrinks = response.json()

# ***UNCOMMENT THIS LINE AND RUN CODE TO SEE A LIST OF ALL CURRENT DRINKS ON API*** (optional)
# pp(allDrinks)



# Where the coding section starts (below)

# function for finding more results:
def moreResults(userSearch):
    # ask the user if they want more results (up to 10 based on api)
    usersChoice = input(f"Would you like to see up to 10 results based on '{userSearch}'\nYes (y) No (n) or Main Program (b) ").lower()

    # if they choose yes:
    if (usersChoice == "y" or usersChoice == "yes"):
        searchedCocktailUrl = f'https://cocktail-by-api-ninjas.p.rapidapi.com/v1/cocktail?name={userSearch}'

        # get the response based off the users choice from previous function
        searchedResponse = requests.get(searchedCocktailUrl, headers = searchedCocktailHeader)

        # Jsonify the results returned from API
        searchedCocktail = searchedResponse.json()

        # IF searchedCocktail is valid (meaning response gives something)
        if searchedCocktail:

            # print the drinks that relate to the users previous search
            print(f"\n\nHere are the drinks that relate to '{userSearch}':")

            # since the results we get back from this seperate api comes in a list, we need to run through every item in the list and print it out, in this case its running through the names
            for cocktail in searchedCocktail:

                # gets every name in the searchedCocktail list (api data)
                name = cocktail.get('name')

                # prints the names with a - before it so its neater
                print(f"- {name}")
            
            # allow user to find ANOTHER drink based on the related search results (optional)
            findSpecificDrinkByName()
        
        # ELSE, the drink name did not return a valid response, there fore they are given this response (should never happen because we cant get to this function without a valid drink in the first place)
        else:
            print(f"No drinks found with the name '{userSearch}'")

    # else if the user says no, just give them a goodbye message and kick them out
    elif (usersChoice == "n" or usersChoice == "no"):
        print("Goodbye!")
    
    # else if the user wants to go back to main, we send them there
    elif (usersChoice == "b" or usersChoice == "main program" or usersChoice == "main"):
        mainProgram()

    # ANY OTHER CASE (else) their choice was not an option and they are sent back to the findSpecificDrinkByName() function.
    else:
        print(f"{usersChoice} was not an option, redirecting to Find By Name")
        findSpecificDrinkByName()

# find specific drink by name function defined here
def findSpecificDrinkByName():

    # ask user to input a drink name
    drinkName = str(input("Enter Drink Name! or Quit (q) ")).lower()

    # using URL to fill in the end point based on the users input
    searchedCocktailUrl = f'https://cocktail-by-api-ninjas.p.rapidapi.com/v1/cocktail?name={drinkName}'

    # get back the data
    searchedResponse = requests.get(searchedCocktailUrl, headers = searchedCocktailHeader)

    # Jsonify the data:
    searchedCocktail = searchedResponse.json()

    # TRY block to catch any key errors
    try:

        # IF the user quits, print goodbye
        if (drinkName == "q" or drinkName == "quit"):
            print("goodbye!")

        # Else IF: user goes back to main, send them to main program
        elif(drinkName == "b" or drinkName == "main program" or drinkName == "main"):
            mainProgram()

        # ELSE IF: searchedCOcktail is valid (returns code 200) then:
        elif (searchedCocktail):

            # automatic message to show user their search
            print(f"Here is the results for the drink you searched for '{drinkName}': ")

            # reach into the overarching list, which has the dictionary inside which contains the info we need (ingredients name instructions)
            cocktail = searchedCocktail[0]

            # naming variables based on dictionary within the list (see above)
            name = cocktail['name']
            ingredients = cocktail['ingredients']
            instructions = cocktail['instructions']

            # Here we are printing the cocktail name
            print(f"Cocktail-Name: {name}\n")

            # herer we are printing the cocktail ingredients
            print("Cocktail-Ingredients:")

            # since the ingredients are in a LIST, we have to iterate through the list, and print out each ingredient INDIVISUALLY
            for ingredient in ingredients:
                print(f"- {ingredient}")

            # formatted instructions variable using textwrap.fill()
            # basically makes it so that the text will wrap rather than keep going on one line indefintley 
            prettyInstructions = textwrap.fill(instructions, width= 60)
            # finally we just print out the formatted instructions
            print(f"\nInstructions:\n{prettyInstructions}")

            # Then we send the user to the moreResults page, to determine if they want more results similar to their search (unless their search is an exact drink)
            moreResults(drinkName)

        # else, no drink was found with that name (doesnt exist in DB)
        else:
        
        # send them back to the top of the function as ask them again
            print(f"No drink found with the name {drinkName}\n")
            findSpecificDrinkByName()
    
    # except if there is a key error (aka they enter a empty string or something like that)
    except KeyError:
        print(f"{drinkName} was not valid, try again!\n")

        # if that happens we send them back to start of function
        findSpecificDrinkByName()

# Here the user is given the choice to find another drink if they decide they dont like the drink they chose
def lookUpDifferentDrink():

    # asks user if they are interested in finding another drink
    findAnotherDrink = input("Find another drink? Yes: (y) No: (n)\n").lower()

    # if the users choice was YES, they are then sent back to the main program where they can repeat the process of finding a drink
    if (findAnotherDrink == "y" or findAnotherDrink == "yes"):
        mainProgram()
    
    # if the users choice was NO, they are kicked out of the program and left with a "goodbye" message as well as their recipe
    elif (findAnotherDrink == "n" or findAnotherDrink =="no"):
        print("Enjoy Your Cocktail!")
    
    # ELSE: if they input ANYTHING other than Yes or No, they are told their choice was not valid, and they are then sent to the start of THIS function and asked again
    else:
        print(f"{findAnotherDrink} was not valid, Try Again!")
        lookUpDifferentDrink()

# Here we take in the users choice of drink (based on the ID inputted)
# further explanation: The parameter (id) can be named ANYTHING, but it will always hold the value of (or represent) the users-input from the function--> askForDrinkId()
def drinkRecipe(id):
        
        # here we define the recipe url as a variable, and pass in the users-input (aka id from the parameter --> drinkRecipe( **id** ) as the endpoint so that we can get back data from the API
        detailedRecipeUrl = f"https://the-cocktail-db3.p.rapidapi.com/{id}"

        # get back our response (which will be 200 if it worked correctly)
        response = requests.get(detailedRecipeUrl, headers=apiHeader)

        # reponse is then "parsed" (aka converted into a readable object (aka dictionary)) which we set to "results" variable
        results = response.json()

        # We then PRETTY-PRINT the results so that it looks nice and formatted on the users screen
        # pp(results)

        # So instead of doing pp(results) and just giving the use a json dictionary, below we have seperated the indivisual parts of the "results" so that we can have a more organized output for the user!
        # (uncomment the "pp(results)" line above to see what i mean)

        # title variable
        title = results['title']

        # ID variabke
        drinkID = results['id']

        # difficulty variable
        difficulty = results['difficulty']

        # ingreddinets variable
        ingredients = results['ingredients']

        # method variable
        method = results['method']

        # here we are using json.dumps, a function in python that makes json objects prettier(more readable) when printed

        # takes in the array(variable we created based on the result of given data), and indents it by 4 while also listing them out as a json-object rather than it ALL being printed out on one line
        recipe = json.dumps(ingredients, indent = 4)
        howTo = json.dumps(method, indent = 4)
        
        # here we are using the imported moduel textwrap(). This basically does what its name implies, it wraps the text from going past a certain width so that its not a whole paragraph displayed in one never ending line.

        # description variable
        description = results['description']

        # formatted description variable using textwrap.fill()
        prettyDescription = textwrap.fill(description, width= 70)

        # here is what the user will see when the code is run rather than "pp(results)"
        print(f"\n\nYou chose the drink: {title}, Drink ID: {drinkID}\n\nDrink Description:\n{prettyDescription}\n\nDrink difficulty is: {difficulty}\nTime required: {results['time']}\n\nIngredients You'll Need!:\n {recipe}\n\n**Creating The Cocktail**\n\n{howTo} ")


        # Finally the user is then sent to lookUpDifferentDrink() function which will basically ask them if they want to find another drink
        lookUpDifferentDrink()
    
# Here the user will have the option to roll another random recipe (or not to)
def rollAnotherRandomRecipe():

    # here we are using Try{}-Except{} logic to catch any "value-errors" (explanation: Try{} will do everything within it, if there happens to be a "Value-Error" it will stop and go to the Except{} which will run whatever is within the except (will explain in code below))
    try:
        # TRY: pogram will prompt user asking if they want to generate another random recipe (.lower() to make sure no matter what they type in, it will come back as lowercase)
        userChoice = str(input("Would you like to generate another random recipe? Yes: (y) No: (n) Main Program = (b)\n")).lower()

        # if the user chooses to generate a new drink, we send them back the the function generateRandomDrink()...(Ctrl or Cmnd + Click on function to automatically go to it (or just scroll to it))
        if (userChoice == "y" or userChoice == "yes"):
            generateRandomDrink()

        # else if: the users choice was to go back to the main program (b), they will be sent back to the very start (aka the first function in order of events) and start from the top essentially (Ctrl or Cmnd + Click on function to automatically go to it)
        elif (userChoice == "b"):
            mainProgram()

        # else if: the users choice is not to generate a new recipe (meaning they like whichever one they landed on), they are kicked out of the program and are left with a "goodbye" message and their recipe
        elif (userChoice == "n" or userChoice == "no"):
            print("Goodbye!")
        
        # Else: ANYTHING they type other than the available options will NOT be valid and they will get a message explaining that
        # After the message is recieved, the user will be sent back to the very start of THIS function--> rollAnotherRandomRecipe() and will be asked again their choice
        else:
            print(f"{userChoice} was not valid, Try Again! \n")
            rollAnotherRandomRecipe()  
        
        # EXCEPT: If the user were to try to type in a number, when the input specifically requires a string, the program will stop running the TRY{block of code} and will run EXCEPT{block of code}

    # EXCEPT: if there was a value error (aka they typed in a number or symbol or anything that wasn't a string) they will be informed that their choice was not valid and will be sent back to the start of THIS function rollAnotherRandomRecipe()
    except ValueError:
        print(f"{userChoice} was not valid, Try Again!")
        rollAnotherRandomRecipe()

# Here is where the user will land if they selected to find a specific drink recipe
def HowToSearchForDrink():

    # immediatley the user is given the List of Drinks to choose from
    # showListOfDrinks()

    # will ask the user for the drinks id (which will be a list available in the read me for each drink and its corresponding id (like a menu at a restaurant))
    # we use .lower() to lowercase the users input so that in the if conditions it can be handled as all lowercase
    usersChoice = input("Would you like to search by NAME (n) or Enter ID (L for list) Main Program: (b) Quit: (Q) \n ").lower()

    # Try: will attempt the logic based on what the user inputs (see decent explanation in rollAnotherRandomRecipe() function
    try:

        # if users choice was to quit, they will be kicked out of program and left with a "goodbye" message
        if usersChoice == "q" or usersChoice == "quit":
            print("Goodbye!")
        
        # else if: users choice is to go back to main program we will run the function maainProgram() to take them to very first function
        elif (usersChoice == "b" or usersChoice == "back"):
            mainProgram()

        # else if the user wants to search by NAME:
        elif (usersChoice == "name" or usersChoice == "drink name" or usersChoice == "n"):

            # send user to find drink by name function:
            findSpecificDrinkByName()

        elif (usersChoice == "list" or usersChoice == "l" or usersChoice == "lis"):
            # Shows list of drinks if that what they want!
            showListOfDrinks()

            # then ask them the same thing
            HowToSearchForDrink()
        
        # ANYTHING else the user inputs (aka an ID) will be turned into an INTEGER (because input() by default return strings)
        # then we run a SECOND "try-except" block which will determine if their inputted ID actually exists in the list of ID's
        else:
            # "Nested" or Second Try-Except block (nested meaning its within another try-except block)
            try:

                # turning userschoice into an integer (cause it will come back as a string) (remember that 1 does not === "1")
                usersIdChoice = int(usersChoice)

                # here we are defining the number of drinks that exist on the api (this can be updated so we just go based off the length of data the api call returns when we ask it to list out ALL the drinks)
                numberOfDrinkAvailable = len(allDrinks)

                try:
                    # Check if the entered id actually exists on the list of ID's (we check this by just making sure its within 0-131)
                    if 1 <= usersIdChoice <= numberOfDrinkAvailable:

                        # if the users inputted ID is within 0-131, THEN we send it to the drinkRecipe(*parameter*) function as a parameter
                        drinkRecipe(usersIdChoice)
                    
                    # Else: Input was NOT valid and we specifcally tell them it has to be within 1-132 for their next attempt
                    # then send them back to askForDrinkId() function
                    else:
                        print(f"{usersIdChoice} is not a valid ID. Please enter an ID between 1 and {numberOfDrinkAvailable}.")
                        HowToSearchForDrink()
                except KeyError:
                    print("Check your ApiKey or ApiDocs(Key-Error)")

            # EXCEPT: if the users input was NOT an INT, we give them a try again message and again send them back to askForDrinkID() function
            # Technically i dont think we need this, but if you have a TRY block then you MUST have an EXCEPT block or the code will error out
            except ValueError:
                print(f"{usersChoice} was not a valid Input, Try Again!")
                HowToSearchForDrink()


    # Here is where we handle "VALUE-ERROR" Lets say the user typed "123ABC", normally this would return a red error on the screen because drinkRecipe() function NEEDS ONLY an INT or else it wont work... Here we basically say, based on the users input TRY the code above, if the users input returns a "Value-Error", then we run whatver is inside the EXCEPT block of code (below)
    except ValueError:

        # prints out what the error was about to inform user
        print(f"{usersChoice} was not a valid ID, Try Again!")

        # runs THIS function again askForDrinkId() and basically takes it from the top of the function asking user same question
        HowToSearchForDrink()

# Generating random drink HERE: (done by importing random)
def generateRandomDrink():

    # we use random.randint() in order to get a totally random integer from a range of numbers and set it equal to a variable (randomID)
    # (in this case we start from number 1, and go up till 132) 
    randomID = random.randint(1,132)

    # we use the link provided by the API which takes in an ID normally(see ex. below) We provide the ID based on the randomly generated number (1-132) and it completes our URL for a random drink
    # (EXAMPLE FOR FURTHER EXPLENATION: Normally, the link is: https://the-cocktail-db3.p.rapidapi.com/(ID # GOES HERE) so we use fstring to dyanmically fill in that number with the randomID variable from just above))
    recipeUrl = f"https://the-cocktail-db3.p.rapidapi.com/{randomID}"

    # get back the response from the url (will be a 200 response if it works correctly)
    response = requests.get(recipeUrl, headers=apiHeader)
    
    # here we "parse"(aka turn into json object) and get back our data from API (EXAMPLE: "id": '4 "title": 'name of drink' etc.)
    results = response.json()

    # here we "PRETTY-PRINT" out the random recipe
    # pp(results)

    # SAME PROCESS AS drinkRecipe() Function:
    # title variable
    title = results['title']

    # ID variabke
    drinkID = results['id']

    # difficulty variable
    difficulty = results['difficulty']

    # ingreddinets variable
    ingredients = results['ingredients']

    # method variable
    method = results['method']

    # here we are using json.dumps, a function in python that makes json objects prettier(more readable) when printed

    # takes in the array(variable we created based on the result of given data), and indents it by 4 while also listing them out as a json-object rather than it ALL being printed out on one line
    recipe = json.dumps(ingredients, indent = 4)
    howTo = json.dumps(method, indent = 4)
    
    # here we are using the imported moduel textwrap(). This basically does what its name implies, it wraps the text from going past a certain width so that its not a whole paragraph displayed in one never ending line.

    # description variable
    description = results['description']

    # formatted description variable using textwrap.fill()
    prettyDescription = textwrap.fill(description, width= 70)
    try:
        # here is what the user will see when the code is run rather than "pp(results)"
        print(f"\n\nYou chose the drink: {title}, Drink ID: {drinkID}\n\nDrink Description:\n{prettyDescription}\n\nDrink difficulty is: {difficulty}\nTime required: {results['time']}\n\nIngredients You'll Need!:\n {recipe}\n\n**Creating The Cocktail**\n\n{howTo} ")
    except KeyError:
        print("Check your ApiKey or ApiDocs")

    # here we run the rollAnotherRandomRecipe() Function which will... (Ctrl or Cmnd + Click function to automatically go to it)
    rollAnotherRandomRecipe()

# Show list of drinks function (simple)
def showListOfDrinks():
    # For every drink in allDrinks (data from API)
    for drink in allDrinks:
        
        # create variables for drink Data
        drinkName = drink['title']
        drinkID = drink['id']
        drinkDifficulty = drink['difficulty']

        # printing all that data so it looks pretty :)))
        print(f"Drink Name: {drinkName}")
        print(f"Drink ID: {drinkID}")


def openAndShowImage(image_path):
    img = Image.open(image_path)
    img.show()

# openAndShowImage() #path name needed (not working yet)

# HERE is where the MAIN-PROGRAM starts!!!
def mainProgram():
    
    # first, the program will ask the user if they want to generate a random drink or find a specific drink they like (from the list of 132 drinks)
    #.lower() at the end of input for (case-sensitivity) (aka: so that no matter what they type it will come out lowercase)
    mainProgramChoice = input("Would you like to find a specific drink or generate a random drink? Random (r) Specific (s) Quit: (q) List: (l)\n").lower() 

    # if their choice was random, we run the generateRandom() function (Ctrl or Cmnd + Click on function to automatically go to it (or just find it))
    if (mainProgramChoice == "r" or mainProgramChoice == "random"):
        generateRandomDrink()
    
    # else if: their choice was a specific drink, we run the askForDrinkID() function (Ctrl or Cmnd + Click on function to automatically go to it (or just scroll to it))
    elif (mainProgramChoice == "s" or mainProgramChoice == "specific"):
        HowToSearchForDrink()             
    
    # else if: The users choice was to quit, they are kicked out of the program, and left with a "goobye" message!
    elif (mainProgramChoice == "q" or mainProgramChoice == "quit"):
        print("Goodbye!")
        
    elif (mainProgramChoice == "l" or mainProgramChoice == "list"):
        showListOfDrinks()

    # ANY other thing they type in is not valid, our program runs one way and its intended to be used one way so they are given a message "try again"
    # we also run the main program from the top in order to let the user try again rather than just kick them off and have them run the python file again
    else:
        print(f"{mainProgramChoice} was not an option, Try Again!")
        mainProgram()

# Here is where the user begins when the python file is run, This is the only function we call on its own because it initiates the program!
mainProgram()