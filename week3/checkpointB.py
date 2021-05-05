"""
File: check03b.py

Purpose: Practice classes with Complex numbers.
"""


# TODO: Create your Complex class here!
class Complex:
    # complex class with 2 member variables
    def __init__(self):
        # both set to 0
        self.real = 0
        self.imaginary = 0

    def prompt(self):
        self.real = input('Please enter the real part: ')
        self.imaginary = input('Please enter the imaginary part: ')

    def display(self):
        return print(f'{self.real} + {self.imaginary}i')


def main():
    """
    This function tests your Complex class. It should have a prompt
    and a display member function to be called.

    You should not need to change this main function at all.
    """
    c1 = Complex()
    c2 = Complex()

    print("The values are:")
    c1.display()
    c2.display()

    print()
    c1.prompt()

    print()
    c2.prompt()

    print("\nThe values are:")
    c1.display()
    c2.display()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
