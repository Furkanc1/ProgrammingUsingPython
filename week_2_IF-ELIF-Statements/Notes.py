myNum = input("type the number on the list")
myNumbAsInt = int(myNum)
myList = [10, 20, 30, 40, 50, 60]
if myNumbAsInt in myList:
    print(myNumbAsInt, "is found on the list")
else:
    print(myNumbAsInt, "is not on the list")

myString = input("Enter a String")
# to grab the index of a number you can use:
print(myString, ": is the string")
print(myString[0], ": is the 0th index in your string")
# which will print the 2nd index of the string OR the 3rd letter of the string

# higherLevel Example:
# inside the object braces, 0 represents the starting index
# and the second number represents which index to stop BUT NOT INCLUDE
# myNewString = myString[0:4]

# the third :_ in the object braces represents the Step property
myNewString = myString[0:5:2]



# will print the first 4 letters of your string OR 0 index, 1 index, 2 index, 3 index...
print(myNewString)
print("The following will be index 0-5, NOT indluding 5 (0-4), stepping by 2 (skipping every other)", myNewString)

# example of another more dynamic print statement
exampleNumber = int(input("enter a number!"))

print(f"the number is {exampleNumber} , is that correct??")
