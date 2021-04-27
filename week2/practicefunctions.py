import sys

def prompt_number():

    number = 0
    while number <= 0:
        number = int(input('Enter a positive number: '))
        sys.exit(0)
    return number

def compute_sum(numberOne, numberTwo, numberThree):

    allTogether = numberOne + numberTwo + numberThree
    return allTogether


numberOne = prompt_number()
numberTwo = prompt_number()
numberThree = prompt_number()
sumup_number = compute_sum(numberOne, numberTwo, numberThree)

print('\nThe sum is ' + str(sumup_number))
