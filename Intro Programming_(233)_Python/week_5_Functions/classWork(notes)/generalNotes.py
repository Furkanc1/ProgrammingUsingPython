# Try / Except used for error handling, can use the specific error name to create a guard around something, and let the user know why they are getting an error in print statement:
# ex:
print(2/0)

try:
    print(2/0)
except ZeroDivisionError:
    print("You can NOT divide by ZERO")
print("you made it past the zeroDivision error")

