"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.

Sorts a list of numbers.
"""


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    for item in range(len(numbers) - 1, 0, -1):
        position = 0
        for location in range(1, item + 1):
            if numbers[location] > numbers[position]:
                position = location

        temp_place = numbers[item]
        numbers[item] = numbers[position]
        numbers[position] = temp_place


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    # numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()