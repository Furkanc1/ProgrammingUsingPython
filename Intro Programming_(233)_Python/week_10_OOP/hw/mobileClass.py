"""
1.  Create a python file with a class called "Mobile ()" which will allow us to create new mobile phone objects.

2.  Each phone has 4 attributes:

make
model
OS
color  
3.  As there are many things a mobile phone can do create at least four methods the phone can do, examples can be receiving a call, playing a video etc...Within the methods, use print statements to reflect the actions. One Method should use more than one attribute in its print statement

4.  Create a separate python file to call the Mobile() class and create at least 3 phone objects. 

5. After creating the objects, let each phone perform at least two of the methods and print 
them on the screen

6. Add comments to both files to explain your process

Submit both files. Ensure the file names are unique between the two and one file name indicates  it is the class file. 

Assignments are considered late if submitted post due date and prior to the assignment locking and may be assessed a penalty.  Once locked, the assignment will not be reopened. 
"""

# mobile class:
class Mobile:
    def __init__(self, make, model, os, color):
        self.make = make
        self.model = model
        self.os = os
        self.color = color

# description method
    def description(self):
        print(f"This phone is: {self.make}-{self.model}\nOs: {self.os}\nColor: {self.color}")

# texting method
    def text(self):
        print(f"The {self.make}-{self.model} is currently Texting")

# calling method
    def call(self):
        print(f"The {self.make}-{self.model} is making a Phone-Call")

# facetime method
    def facetime(self):
        print(f"The {self.make}-{self.model} is making a Facetime-Call")

# instagram scrolling method
    def instagram(self):
        print(f"The {self.make}-{self.model} is scrolling through Instagram")