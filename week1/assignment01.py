import random
import sys

guess = ""
count = 0

print("Welcome to the number guessing game!")
seed = input("Enter random seed: ")
random.seed(seed)

mynumber = random.randint(1, 100)

while True:
    count += 1
    guess = int(input("\nPlease enter a guess: "))
    if mynumber == guess:
        print('Congratulations. You guessed it!')
        print(f'It took you {count} guesses.')
        play = None
        count = 0
        mynumber = random.randint(1, 100)
        while play != 'yes' or play != 'no':
            play = input("\nWould you like to play again (yes/no)? ")
            if play == 'yes':
                break
            elif play == 'no':
                print("Thank you. Goodbye.")
                sys.exit(0)
            else:
                print('wrong value, please enter [Yes/No]')
    elif guess < mynumber:
        print('Higher')
    elif guess > mynumber:
        print('Lower')


