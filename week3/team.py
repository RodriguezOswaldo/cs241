class Rational:

    def __init__(self):
        self.numerator = 0
        self.denominator = 1
        self.check = ''
        self.message = ''

    def keep_running(self):
        self.check = input('Do you want to continue playing, [y/n]: ?')
        if self.check == 'y':
            main()
        else:
            print('See you later.')
            pass

    def prompt(self):
        self.numerator = int(input('Enter the numerator: '))
        self.denominator = int(input('Enter the denominator: '))

    @property
    def display(self):
        if self.numerator < self.denominator:
            print('Error! numerator should be larger than denominator.')
            self.keep_running()

        else:
            print(f'{self.numerator} / {self.denominator}')

    def display_decimal(self):
        return print(self.numerator / self.denominator)


def main():
    print('~~~~~~~~~~~~~~~~~~~~')
    new_number = Rational()
    print(f'{str(new_number.numerator)}/{str(new_number.denominator)}')
    new_number.prompt()
    new_number.display
    new_number.display_decimal()


if __name__ == "__main__":
    main()
