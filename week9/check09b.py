# Make a function get_inverse that accepts
# a number  n, and then returns the result 1/n.

def get_inverse(n):
    """
    In the get_inverse function you should check for the
    following rules and raise an appropriate exception.
    Do not display any error messages in this function,
    simply raise the exception.

    n is not a number: ValueError

    """
    if type(n) != int:
        raise ValueError
    elif n == 0:
        raise ZeroDivisionError
    elif n < 0:
        raise NegativeNumberError
    return 1/n


# Create a new exception type: NegativeNumberError
# that inherits from Exception
class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    # In main, prompt the user for the value,
    # then pass it to your get_inverse,
    # and save the result in a variable.
    # Finally, display the result.
    try:
        value = int(input('Enter a number:  '))
        result = get_inverse(value)
    except ValueError:
        print('n is not a number:')
    except ZeroDivisionError:
        print('n is not a number:')
    except NegativeNumberError:
        print('n is less than zero')

    print(result)


if __name__ == '__main__':
    main()