# Course: Introduction to Programming (INFO-233)
# Student Name: 

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.


#HINT: to output your work to the screen, you must use print()


################################
# Problem 1: Fun With Strings
################################

### Part A ###

# Use substring notation to extract the word "box" from the variable below.

# WHAT IS SUBSTRING?:
# substring notation: Variable[ 0 : 4 : 2] (includes position 0 and excludes position 4 (so 3 is the stopping point))
# the third paramter is 2, the Stepping Property which is how many you want to skip over

# EX OF SUBSTRING BELOW:
# renamed phrase variables for better readability
phrase = "Life is like a box of chocolates."

print(phrase[15:18])
# will print in terminal "box"




### Part B ###

# There is a secret code in the variable phrase. It can be found by extracting
# every third character. Write the Python code necessary to extract these
# characters and print the results.

phrase2 = "I2FNB3F77OVB-PJ2BB3ZQ3BV"

# we do starting index 0, ending index 25(1 more than expected to get all the values) and STEP by 3 so every 3 
# starts from 0 index, goes until 25th (1 more than expected) and Steps or Skips over every 3
print(phrase2[ 0 : 25 : 3])
#  will print in terminal "INFO-233"


### Part C ###

# Does any version of the ```word``` "new" occur in the variable phrase? Assume this
# means case insensitive. 

#  tehcnically speaking the STRING "new" does not occur in this phrase, but the word it self does (kinda confused what to do here)
# What I did: Made the phrase lowercase so it wont check case sensitivity, Could also have made uppercase, then put the new variable in my if-statement (searched up .lower() method )
phrase = "UnIqUe NeW YoRk"
lowercasePhrase = phrase.lower()

new = "new"

if new in lowercasePhrase:
    print("the word `new` is in the phrase.")
else: print("the word `new` is NOT in the phrase")

# if the variable new = "new", will go with sucess condition not else 


########################
# Problem 2: Conditional Statements
########################

# A password must be between 6 and 13 characters. Write Python code to determine
# whether the passwords below meets the necessary length requirements.

### Part A ###

password1 = 'Nope'
#  IF length(of password) is <= 5 : PRINT (too short)
if (len(password1) <= 5):
    print("Your Password Must Be Atleast 6 Characters!")
# IF length(of password) is >= 14 : PRINT (too long)
elif(len(password1) >= 14):
    print("Your Password Must Be Atmost 13 Characters!")
# else the password has to be correct, so (accept)
else: print("Password Accepted!")

### Part B ###
# same logic as above
# code:
password2 = 'Maybe???'

if (len(password2) <= 5):
    print("Your Password Must Be Atleast 6 Characters!")
elif(len(password2) >= 14):
    print("Your Password Must Be Atmost 13 Characters!")
else: print("Password Accepted!")


### Part C ###
# using the same logic through out homework, if the password length is less than or = 5, too short // if pass >= 14, too long 

# code:
password3 = 'Wayyyyy Too Longgggg'

if (len(password3) <= 5):
    print("Your Password Must Be Atleast 6 Characters!")
elif(len(password3) >= 14):
    print("Your Password Must Be Atmost 13 Characters!")
else: print("Password Accepted!")