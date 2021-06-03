"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

# Import anything you need for Abstract Base Classes / methods
from abc import ABC, abstractmethod


# convert this to an ABC
class Shape(ABC):
    def __init__(self):
        self.name = ""

    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))

    # Add an abstractmethod here called get_area
    @abstractmethod
    def get_area(self):
        raise NotImplementedError('Subclass must implement abstract method')


# Create a Circle class here that derives from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.name = 'Circle'
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


# TODO: Create a Rectangle class here that derives from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.name = 'Rectangle'
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


def main():

    # Declare your list of shapes here
    shapes = []

    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            # Declare your Circle here, set its radius, and
            circle = Circle(radius)
            circle.get_area()
            # add it to the list
            shapes.append(circle)

        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            # Declare your Rectangle here, set its length
            # and width, and add it to the list
            rectangle = Rectangle(length, width)
            rectangle.get_area()
            # add it to the list
            shapes.append(rectangle)

    # Done entering shapes, now lets print them all out:

    #  Loop through each shape in the list, and call its display function
    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()
