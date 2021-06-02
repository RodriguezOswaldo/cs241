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
    def __init__(self):
        self.name = 'Circle'

    def get_area(self):
        pass


# TODO: Create a Rectangle class here that derives from Shape
class Circle(Shape):
    def __init__(self):
        self.name = 'Rectangle'

    def get_area(self):
        pass


def main():

    # TODO: Declare your list of shapes here

    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            # TODO: Declare your Circle here, set its radius, and
            # add it to the list

        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            # TODO: Declare your Rectangle here, set its length
            # and width, and add it to the list

    # Done entering shapes, now lets print them all out:

    # TODO: Loop through each shape in the list, and call its display function


if __name__ == "__main__":
    main()
