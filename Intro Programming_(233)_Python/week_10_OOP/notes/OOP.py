# Object Oriented Programming Day 1 

# In-Class Example:

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"The {self.make}-{self.model} is Driving")

    def stop(self):
        print(f"The {self.make}-{self.model} is Stopped")


