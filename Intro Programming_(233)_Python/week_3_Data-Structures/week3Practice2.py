# -*- coding: utf-8 -*-
"""
methods and functions in Python function are used on while methods are applied to objects. 
Functions essentially take objects as inputs while methods act on objects.

"""

# For example sort() while it looks like a function it is actually a method
# fruit = ['apple', 'pear', 'banana', 'orange', 'grapes']
# print(fruit)

# fruit.sort()
# print(fruit)

# while length is a function in python 

# print (len(fruit))

#notice the sytax difference. and notice the period when calling a method?

""" OK, let's have soime fun with lists. There are comments below which explain the challenge. Code the requirements and run it to see if you get the correct answers
"""

########### Challenge 1 #########################

mylist = [5, 10, 15, 20, 25, 50, 20]

# find the value 20 in the list and replace it with 200
# print the list in it's orginal version
# next  use the  index() medthod to find the 20 and assign it to a variable
# update the the list using [] and the variable for the indexed value
""" Expected output 
[5, 10, 15, 20, 25, 50, 20]
[5, 10, 15, 200, 25, 50, 20]
"""
print(mylist)
# selecting index of First #20, = 3
selectedNumber = mylist.index(20)
# from "myList" we are grabbing the index of 20 and reassigning its value to 200 INT
mylist[selectedNumber] = 200
print(mylist)


########### Challenge 2 #########################
mylist2 = [10.2, 10, 11.5, 8.3, 7.2]

#print the type of the list
#print the type of the second element
#print the type of the last element
# Is there another way to print the last last element
""" Expected output
<class 'list'>
<class 'int'>
<class 'float'>
<class 'float'>
<class 'float'>
"""
print(type(mylist2))
print(type(mylist2[0]))
print(type(mylist2[1]))
print(type(mylist2[2]))
print(type(mylist2[3]))
print(type(mylist2[4]))




# SAME AS ABOVE BUT ITS MORE DRY CODE (for loops are so much easier it seems in python than Javascript wow)

# dataType = my own variable
# for dataType in mylist2:
#     print(type(dataType))


########### Challenge 3 #########################
#update mylist2 by adding the number 5.6 to the end and print my list 2

""" Expected output

[10.2, 10, 11.5, 8.3, 7.2, 5.6]

"""
newNumberToAppend = 5.6
mylist2.append(newNumberToAppend)
print(mylist2)

########### Challenge 4 #########################
# using mylist2, select elements 2,3,4 and print it

""" Expected output
[10, 11.5, 8.3]
"""
selectedElementsFromList = mylist2[1:4]
print(selectedElementsFromList)

########### Challenge 5 #########################
# Select the last element of mylist2 and store it in a variable named last_element
#multiply the last elelment by 6 and append it to the end of my list 2 as an integer and print mylist2

""" Expected output
[10.2, 10, 11.5, 8.3, 7.2, 5.6, 33]
"""

selectedElementForMultiplication = mylist2[-1]
# we use INT ehre because it iwll return like 33.334343434353434 rather than the clean whole number
newListNumber = int(selectedElementForMultiplication * 6)
mylist2.append(newListNumber)
print(mylist2)

########### Challenge 6 #########################
#remove 33 from mylist2 and print it

""" Expected output
[10.2, 10, 11.5, 8.3, 7.2, 5.6]
"""
# selecting index of -1 (last elemtn in list) to pop or remove. (same in JS)
mylist2.pop(-1)
print(mylist2)