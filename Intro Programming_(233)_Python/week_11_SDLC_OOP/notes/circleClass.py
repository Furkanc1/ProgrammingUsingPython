# Creating a Circle Class

# import math to use math.pi for 3.1415.....
import math

# creation of Circle Class
class Circle:
    # create the circle object, taking in radius as a parameter
    def __init__(self, radius):
        # defining the radius parameter as the objects self.radius
        self.radius = radius
    
    # find perimeter function: (taking in the object(self) as parameter)
    def findPerimeter(self):

        # perimeter found using simple math equation: 2*pi*r (round it to 2 decimals)
        perimeter = round((2 * math.pi * self.radius), 2)
        
        return perimeter
        # print statement: to give perimeter value
        # print(f"Based on the radius: {self.radius}, the perimeter is {perimeter} ")

    # find area function: taking in object(self) as parameter
    def findArea(self):

        # area found using equation PI * R^2 (round it to 2 decimals)
        area = round(( math.pi * (self.radius * self.radius)), 2)
        return area
        # print statement: to give area value
        # print(f"Based on the radius: {self.radius}, the area is: {area} ")