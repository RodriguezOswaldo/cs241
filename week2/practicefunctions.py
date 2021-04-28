def prompt_number():
    number = int(input("Enter a positive number: "))
    while number <= 0:
        print("Invalid entry. The number must be positive.")
        number = int(input("Enter a positive number: "))
    if number > 0:
        print('')

    return number


def compute_sum(number_one, number_two, number_three):
    all_together = number_one + number_two + number_three
    return all_together


def main():
    number_one = prompt_number()
    number_two = prompt_number()
    number_three = prompt_number()
    total = compute_sum(number_one, number_two, number_three)
    print('The sum is: ' + str(total))


if __name__ == "__main__":
    main()
