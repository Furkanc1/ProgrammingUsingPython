# import circleCLass from circle
from circleClass import Circle

# circle 1 takes in 5 as radius and sends it to the object
circle1 = Circle(
    5
    # can do input() and change to float for this rather than 5
)
# circle 2 takes in 7.5 as radius and sends it to the object

circle2 = Circle(
    7.5
)

# here we use the circls, and send them into the functions we want use (area / perimeter)
print(f"\nCircle 1 area: {circle1.findArea()}\nCircle 1 perimeter: {circle1.findPerimeter()}\n\nCircle 2 area: {circle2.findArea()}\nCircle 2 perimeter: {circle2.findPerimeter()} ")


# circle1.findArea()
# circle1.findPerimeter()

# print(f"\nCircle 2: ")
# circle2.findPerimeter()
# circle2.findArea()