# Make a list for odd numbers and one for even numbers.
even = []
odds = []

# Ask the user for numbers and put them in the appropriate list.
# Create a loop that prompts the user for a number (0 to quit).
add = None
while add != 0:
    try:
        add = int(input('Enter a number (0 to quit): '))
        if add > 0 and (add % 2) == 0:
            even.append(add)
        elif add > 0 and (add % 2) != 0:
            odds.append(add)
    except ValueError:
            print('add an odd or even number')
print()
print('Even numbers:')
for i in even:
    print(i)
print()
print('Odd numbers:')
for i in odds:
    print(i)
