def prompt():
    person = Person()
    person.first_name = input('Enter first name: ')
    person.last_name = input('Enter last name: ')
    person.age = int(input('Enter age: '))
    person.eyes_color = input('Enter eyes color: ')
    person.hair_style = input('Enter hair style: ')
    return person


def print_user(person):
    print('your information: ')
    print(f'{person.first_name} {person.last_name} your age is {person.age}.')
    print(f'The color of your eyes is {person.eyes_color}. Your hair style is {person.hair_style}')


class Person:

    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.age = ''
        self.eyes_color = ''
        self.hair_style = ''


def main():
    person = prompt()
    print_user(person)


if __name__ == '__main__':
    main()
