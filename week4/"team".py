class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000

    def prompt(self):
        # minimum = 1
        # maximum = 12
        self.month = 0
        self.day = int(input('Day: '))
        # second try
        # while self.month < minimum or self.month > maximum:
        #     # self.month = int(input('Month: '))
        #     if self.month < minimum or self.month > maximum:
        #         self.month = int(input('Month: '))
        #         print('Month must be an integer between 1 and 12')
        #     else:
        #         pass
        # first try
        # if self.month > 12:
        #     print('Month cannot be higher than 12')
        #     self.month = int(input('Month: '))

        self.month = int(input('Month: '))
        self.year = int(input('Year: '))

    def display(self):
        print(f'{self.month}/{self.day}/{self.year}')


class Assignment:
    def __init__(self):
        self.name = 'Untitled'
        self.start_date = Date()
        self.due_date = Date()
        self.end_date = Date()

    def prompt(self):
        self.name = input('Name: ')
        print()
        print('Start Date: ')
        self.start_date.prompt()
        print()
        print('Due Date: ')
        self.due_date.prompt()
        print()
        print('End Date: ')
        self.end_date.prompt()
        print()

    def display(self):
        print(f'Assignment: {self.name}')
        print('Start Date:')
        self.start_date.display()
        print('Due Date:')
        self.due_date.display()
        print('End Date:')
        self.end_date.display()
        return


my_date = Date()
my_date.prompt()
print(my_date.month)
my_date.display()

# def main():
#     my_assignment = Assignment()
#     my_assignment.prompt()
#     my_assignment.display()
#
#
# if __name__ == "__main__":
#     main()
