# Functions are formatted as follows:

# Def = definition (same as let in JS) // functionName = any variable to name the function // INSIDE the '()' is where we can put parameters
def functionName():
    # Inside is what the function runs when its called
    print('this is a function!')

# Calling a function :
functionName()

# In-Class Practice (professor example): 

# first Define the function (try to define functions at the top of the file and call / use functions last)
# Basically when salesTax is called, it will be expecting a parameter named cost, but can be ANYTHING ( "salesTax(anyVariable)" ) and it defines "taxRate" variable as well as "tax" variable and tax is defined as "cost * taxRate" (continued below)
def salesTax(cost):
    taxRate = 0.0625
    tax = round(cost * taxRate, 2)
    # cost in this print statement is not defined yet technically until we create a Variable below to pass into the function as a parameter which will represent (cost).
    print(f"The tax for {cost} is {tax}")
    return tax

# Main program:

# we define a new variable price which expects a user input and turns into a float
price = float(input("Please enter the cost of an item!"))

# we then call the function down here using the newly created "price" variable as the parameter expected in the function
# when this "salesTax(price)" runs, it will take price and just redefine it as "salesTax(cost)" where (cost) is just representing the variable (price)
salesTax(price)

# We can continue this by creating variables using the functions:
actualTax = salesTax(price)
print(f"(same output but) -> Redfining variable 'tax' \ as 'actualTax' below:")
print(f"The tax on ${price} is ${actualTax}")

# and even further:
totalPrice = round(price + actualTax, 2)
print(f"The item will cost: ${totalPrice}!")




# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# My attempt at a similar program (for calculating price with 30% discount)

# define function name: // Accept parameter of "originalCost"
def thirtyPercentOff(originalCost):
    # percent you need to actually multiply by to get the percentage the customer is paying
    percentToMultiplyBy = 0.70
    # define newPrice as the original cost * the percentToMultiplyBy
    newPrice = round(originalCost * percentToMultiplyBy, 2)
    # print out the original price and what the price is after the 30% off
    print(f"The original price was ${originalCost}, and with thirty percent off, you are paying ${newPrice}")

# define the parameter as a user input for "the original cost of an item"
originalPriceUserInput = float(input("Enter Original Cost of Item! "))

# Call the function and insert the users input(originalPrice) as the parameter which is then represented by "(originalCost)" inside the function above
thirtyPercentOff(originalPriceUserInput)