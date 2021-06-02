class Student:
    def __init__(self):
        self.name = ''
        self.course = ''

    def prompt(self):
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Please insert name and course code. ')
        self.name = input('Enter name: ')
        self.course = input('Enter course: ')
        print('~~~~~~~~~~~~~~~~~~~\n')

    def display(self):
        print('-------------------------------------------------')
        print(f"{self.name} needs help with her {self.course} course")
        print('-------------------------------------------------\n')


class HelpSystem(Student):
    def __init__(self):
        super().__init__()
        self.waiting_list = []

    def is_student_waiting(self):
        if len(self.waiting_list) > 0:
            return True
        else:
            print()
            print('Is there any student in the waiting list?')
            return False

    def add_to_waiting_list(self):
        super().prompt()
        self.waiting_list.append(self.name)
        super().display()

    def help_next_student(self):
        if self.is_student_waiting():
            self.waiting_list.pop()
            print('-------------------------------------------------')
            print(f'Now helping {self.name} with {self.course}')
            print('-------------------------------------------------')
            self.is_student_waiting()

        else:
            print('No one to help')

    def checking(self):
        check = input('Do you want to help next student?: [Yes/No]')
        if check == 'Yes':
            self.help_next_student()
        elif check == 'No':
            print('Ok, see you later alligator.')
            pass


def main():
    print('Options')
    print('1. Add new Student')
    print('2. Help next Student')
    print('3. Quit')
    option = input('choose your option')
    if option == 1:
        print('Here is the option 1')
    elif option == 2:
        print('Here is the option 2')
    elif option == 3:
        print('See you later!')
    #      system = HelpSystem()
    # print(system.is_student_waiting())
    #
    # system.add_to_waiting_list()
    # print(system.is_student_waiting())
    # system.checking()
    # print(system.is_student_waiting())


if __name__ == '__main__':
    main()
