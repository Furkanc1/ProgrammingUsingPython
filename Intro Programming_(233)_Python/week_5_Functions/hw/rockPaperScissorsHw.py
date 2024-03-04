# Dictionary of the choices and what their abilities are :
choiceOptionsDictionary = {
    'rock': "The rock is able to break the scissors, but can be defeated by the paper",
    'paper': "The paper is able to wrap the rock up, but is easily cut by the scissor",
    'scissor': "The scissor is able to cut paper, but is smashed by the rock"
}
# defining the valid choices a user is allowed to put in:
choicesAccepted = ('rock', 'paper', 'scissor')

# defining a function "askUser" which will:
def askUser():
    # prompy user to enter one of the following choices (and lowercases it to account for user error)
    usersInput = input("Please choose: Rock, Paper, or Scissors: ").lower()

    # if the users input is included in the tuple "choicesAccepted" then:
    if usersInput in choicesAccepted:
        # print the information which corrolates to the information in the dictionary using its [usersInput] as the index
        print(f"Here is the information on: {usersInput}, {choiceOptionsDictionary[usersInput]}")
    # if the user puts the letter Q, this will end the game and print goodbye!
    elif(usersInput == "q"):
        print("Thanks for playing...goodbye! ")
    # finally if the user does anything other than the acepted parameters, the print will tell them that their input was invalid and to input one of the choices inside the tuple OR Q to quit
    else:
        print(f"Sorry, {usersInput} is not a valid choice, please enter one of the following: {choicesAccepted} or `Q` to quit!")
        # Finally finally, the function will be called and run again here so the user doesnt have to manually rerun the python file every time they mess up:
        askUser()

# call the function for the first time when the python file is run 
askUser()

