# NOTES CONTINUED ( ARGS ) :

# *args allows you to feed in as many parameters you want 
def sumOfAll(*args):
    # define total as 0 (starting point)
    total = 0
    # for loop: for every passed in variable into the parameter -> "(*args)"
    for args in args:
        # redefine the total as : 0 or the original total + whatever variable is passed in for args (see totalNumbers variable below)
        total = total + args
    # return whatever the output of the function was for later use (not sure if it applies in this case)
    return total

# NEED TO WORK ON THIS (specifically just error handling for if they enter a string rather than a number)
def howManyNumbers():
    amountOfNumbers = input("How Many Numbers Do You Want To Add?")
    numbersToAdd = int(amountOfNumbers)
    if(numbersToAdd == str):
        print("You must enter a *NUMBER*, of *ATLEAST 2*")
        howManyNumbers()
    elif (numbersToAdd == 2):
        firstNumber = int(input("Enter First Number"))
        secondNumber = int(input("Enter Second Number"))
        total = sumOfAll(firstNumber, secondNumber)
        print(f"The SUM of your numbers is {total}")
    elif (numbersToAdd == 3):
        firstNumber = int(input("Enter First Number"))
        secondNumber = int(input("Enter Second Number"))
        thirdNumber = int(input("Enter Third Number"))
        total = sumOfAll(firstNumber,secondNumber,thirdNumber)
        print(f"The SUM of your numbers is {total}")
    elif (numbersToAdd == 4):
        firstNumber = int(input("Enter First Number"))
        secondNumber = int(input("Enter Second Number"))
        thirdNumber = int(input("Enter Third Number"))
        fourthNumber = int(input("Enter Fourth Number"))
        total = sumOfAll(firstNumber,secondNumber,thirdNumber, fourthNumber)
        print(f"The SUM of your numbers is {total}")
    elif (numbersToAdd == 5):
        firstNumber = int(input("Enter First Number"))
        secondNumber = int(input("Enter Second Number"))
        thirdNumber = int(input("Enter Third Number"))
        fourthNumber = int(input("Enter Fourth Number"))
        fifthNumber = int(input("Enter Fourth Number"))
        total = sumOfAll(firstNumber,secondNumber,thirdNumber, fourthNumber, fifthNumber)
        print(f"The SUM of your numbers is {total}")
    elif (numbersToAdd >= 6):
        print(f"{numbersToAdd} is too high of a number, havent coded for it yet, Try a lower number...")

howManyNumbers()


# totalNumbers = sumOfAll(1, 2, 3, 4, 5, 6)
# print(f"The total of the numbers = {totalNumbers}!")