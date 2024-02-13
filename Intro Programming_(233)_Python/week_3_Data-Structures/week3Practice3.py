# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 11:23:21 2022

@author: john
"""

""" Lets have some fun with dictionaries with a few challenges"""

#### Challenge 1 ##########
# create your first dictionary from two existing lists, one called keys and one called values ## HINT: Research zip()

keys = ('square','triangle','octogon','pentagon')
values = (4,3,8,5)

""" Expected Output 
{'square': 4, 'triangle': 3, 'octogon': 8, 'pentagon': 5}

"""
# tuple is pretty confusing here is a definition for it: 
# The main difference between the two is that tuples are immutable, meaning they cannot be changed once they are created.

# zip will combine the two tuples which is defined by my variable newDictionary
# dict() is a constructor which will combine the two as a dictionary (or in better terms key value pairs)
newDictionary = dict(zip(keys, values))
print(newDictionary)




#### Challenge 2 ##########

# how many key:value pairs are in your dictionary?
# dump your dictionary keys
# dump your dictionary values

""" Expected Output 
There are 4 items in the dictionary
dict_keys(['square', 'triangle', 'octogon', 'pentagon'])
dict_values([4, 3, 8, 5])
"""

lengthofDictionary = len(newDictionary)
print(f"there are {lengthofDictionary} items or key value pairs in the dictionary!")

# list will list out the value inside the parenthesis in this case reaching into my dictionary and selecting zipped values of "keys and values"
print(f"dict_keys({list(newDictionary.keys())})")
print(f"dict_keys({list(newDictionary.values())})")

#### Challenge 3 ##########
# how many sides does an octogon have ? Select and print out the value of Octogon
""" Expected output
An octogon has 8 sides.
"""

octogonSides = newDictionary['octogon']
print(f"an octogon has, {octogonSides} sides!")

triangleSides = newDictionary['triangle']
print(f"a triangle has, {triangleSides} sides!")



#### Challenge 4 ###########
#Is there a nonagon in the dictionary? use an if statment to test the dictionary and if it is there, print it and if it is not print a statement to let me know


""" Expected Output
A nonagon is not in my_dictionary

"""
# THIS WORKS BUT I DIDNT WANT IT TO KEEP RUNNING EVERYTIME I TEST MY CODE SO ITS COMMENTED OUT!
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# isItInTheDictionary = input("type a shape to determine if it is inside the dictionary! ")
# if isItInTheDictionary in newDictionary:
#     print(f"{isItInTheDictionary} is in the dictionary! ")
# else: 
#     print(f"{isItInTheDictionary}, is NOT in the dictionary. SORRY!")
      

#### Challenge 5 ###########

#now modify the code from Challenge 4 so that the program asks a user for the shape to search for. Print the appropriate output as shown

# be sure to test both a true and a false statement

""" Expected Output


What shape do you want to search for in our doctionary? square
I found your shape . A square has 4 sides

What shape do you want to search for in our doctionary? nonagon
Sorry, nonagon isn't in my dictionary
"""
# must return the string as lowercase so that we dont run into a syntax error while reaching into the dictionary
# "triangle" is not === "Triangle" because of case sensitivity so we adjust for user error by automatically makign it lowercase (SAME AS EMAILS)
isItInTheDictionary = input("type a shape to determine if it is inside the dictionary! ").lower()


if isItInTheDictionary in newDictionary:
    usersSelectedShapeSides = newDictionary[isItInTheDictionary]
    print(f"{isItInTheDictionary} is in the dictionary... the {isItInTheDictionary} has {usersSelectedShapeSides} sides!")
else: 
    print(f"{isItInTheDictionary}, is NOT in the dictionary. SORRY!")


# if isItInTheDictionary in newDictionary:
#     print(f"{isItInTheDictionary} is in the dictionary... the {isItInTheDictionary} has {usersSelectedShapeSides} sides!")
# else: 
#     print(f"{isItInTheDictionary}, is NOT in the dictionary. SORRY!")


#fun with Sets

a = {1,2,3,4,5}
b = {1,2,4,5,7}

# There are two sets above, a & b. Simply write one line of code for each challenge below 

#### Challenge 1 ###########
# one line of code which prints out a set comprised of both a & b
""" Expected Output

{1, 2, 3, 4, 5, 7}

"""
# union method will combine two sets or lists, creating a new set / list / array
combinedSets = (a).union(b)
print(combinedSets)

#### Challenge 2 ###########
# now print the set with only what is in common between a & b
""" Expected Output

{1, 2, 4, 5}

"""
# intersection method will return elements that are in both sets as a new set!
commonElementSet = (a).intersection(b)
print(commonElementSet)



#### Challenge 3 ###########
#now print only the elements contained in a and not b
""" Expected Output

{3}

"""
# difference method will allow you to take elements from on set and compare it to another, whatever is different between the first and the second, will be printed, in this case A is different from B because A contains a 3 and B does not
onlyInAElements = (a).difference(b)
print(onlyInAElements)




#### Challenge 3 ###########
# finally print only the elements contained in b and not in a
""" Expected Output

{7}

"""
# log 7 becausue B contains 7 but A does not 
onlyinBElements = (b).difference(a)
print(onlyinBElements)