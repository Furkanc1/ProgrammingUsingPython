# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 08:44:59 2023

@author: johnk
"""

""" 

What Is the Cost of A New Jersey Speeding Ticket?

Build the traffic court judge program. 
An accused speeder is appearing before a judge in the matter of speeding. The Judge asks the police officer
appearing for the prosecution, "What is the posted speed limit?". The officer answers the judge 
with the posted speed limit for the street the traffic stop occured. The judge then asks
"How fast was the accused going?" The officer recites the dirver's recorded speed. The judge does a
quick calculation and comes up with a decision if the person is speeding over a posted speed limit
and if they are, assign points their drving record and fine them as noted in the table below

Build a Python script to help the judge decide if a person is speeding and if so, print out the points
and fine

Points and fines below:


######## HINTS #########################
1.  Solve this by using your word problem skills. 
2.  A question from the problem is a good case to use the input() function
3.  Use variables to do the calculation to find out how many miles over the speed limit
4.  In coding, the use of the conditional is required to make a decision. Set up the conditional based on the miles over the speed limit
5.  Assign points and fines to a variable based on the speed as evaluated by the conditional. don't forget to assign 0 point and $0.00 fines
if a person was not speeding. 

6.  Save the print statement for the end. 
7.  Test it with the person travelling under the speed limit. Does your code assign 0 points and 0 fines?
if not, fix it to include $0.00 fine and 0 points

8.  Once this works, set up a second conditional to print out the fines and points. If the person was not speeding print out a statement
letting the judge know the driver was not speeding. 
Speed Over Limit	Fine	Points
1-9   mph	        $85	     2
10-14 mph	        $95	     2
15-19 mph	        $105	 4
20-24 mph	        $200	 4
25-29 mph	        $220	 4
30-34 mph	        $240	 5
35-39 mph	        $269	 5

"""
#Lets get the inputs of the two speeds, posted limit and how fast the accused was traveling
# Also calculate the mile over the limit.
speedLimitOnGivenStreet = int(input('Enter speed limit of the `traffic-stop` street '))
accusedSpeederMPH = int(input('Enter MPH of Accused Speeder'))

MPHOverLimit = (accusedSpeederMPH - speedLimitOnGivenStreet)

#Use if elif else to compare the excessSpeed to the points and fines assessed

# using ELIF statement and using ranges of speed to determine to Print output
if (MPHOverLimit <= 0):
    print(f"Accused was NOT over the speed limit :)")
elif (1 >= MPHOverLimit <= 9):
    fine = "$85.00"
    points = 2
    print(f"Accused was {MPHOverLimit} MPH over the limit, They are subject to a(n) {fine} fine, as well as {points} points on their liscence")
elif (10 >= MPHOverLimit <= 14):
    fine = "$95.00"
    points = 2
    print(f"Accused was {MPHOverLimit} MPH over the limit, They are subject to a(n) {fine} fine, as well as {points} points on their liscence")
elif (15 >= MPHOverLimit <= 19):
    fine = "$105.00"
    points = 4
    print(f"Accused was {MPHOverLimit} MPH over the limit, They are subject to a(n) {fine} fine, as well as {points} points on their liscence")
elif (20 >= MPHOverLimit <= 24):
    fine = "$200.00"
    points = 4
    print(f"Accused was {MPHOverLimit} MPH over the limit, They are subject to a(n) {fine} fine, as well as {points} points on their liscence")
elif (25 >= MPHOverLimit <= 29):
    fine = "$220.00"
    points = 4
    print(f"Accused was {MPHOverLimit} MPH over the limit, They are subject to a(n) {fine} fine, as well as {points} points on their liscence")
elif (30>= MPHOverLimit<= 34):
    fine = "$240.00"
    points = 5
    print(f"Accused was {MPHOverLimit} MPH over the limit, They are subject to a(n) {fine} fine, as well as {points} points on their liscence")
elif (MPHOverLimit >= 35):
    fine = "$269.00"
    points = 5
    print(f"Accused was {MPHOverLimit} MPH over the limit, They are subject to a(n) {fine} fine, as well as {points}+ points on their liscence")
else: print('Value Must Be a valid INTEGER')
# shouldnt even get to this else statement because the input only takes integers lol just realizing


