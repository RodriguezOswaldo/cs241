class NegativeNumberError(Exception):
    pass


def get_inverse(n):
    if n < 0:
        raise NegativeNumberError
    return 1/n


def main():

    try:
        value = int(input('Enter a number: '))
        result = get_inverse(value)
        print(f'The result is: {result}')
    except ValueError:
        print('Error: The value must be a number')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
    except NegativeNumberError:
        print('Error: The value cannot be negative')


if __name__ == '__main__':
    main()