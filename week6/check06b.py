class Phone:
    def __init__(self):
        self.area_code = None
        self.prefix = None
        self.suffix = None

    def prompt_number(self):
        self.area_code = int(input('Area Code: '))
        self.prefix = int(input('Prefix: '))
        self.suffix = int(input('Suffix: '))

    def display(self):
        print(f'({self.area_code}){self.prefix}-{self.suffix}')


class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ''

    def prompt(self):
        self.prompt_number()
        self.email = input('Email: ')

    def display(self):
        print('\nPhone info: ')
        Phone.display(self)
        print(f'{self.email}')


def main():
    phone = Phone()
    print('Phone:')
    phone.prompt_number()
    print('\nPhone info:')
    phone.display()

    cellphone = SmartPhone()
    print('\nSmart phone:')
    cellphone.prompt()
    cellphone.display()


if __name__ == '__main__':
    main()
