class BalanceError(Exception):
    pass


class OutOfChecksError(Exception):
    pass


class CheckingAccount:
    def __init__(self, starting_balance, num_checks):
        self.balance = starting_balance
        self.check_count = num_checks

    def deposit(self, amount):
        pass

    def write_check(self, amount):
        pass

    def display(self):
        pass

    def apply_for_credit(self):
        pass


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))

            acc = CheckingAccount(balance, num_checks)
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            amount = float(input("Amount: "))
            acc.write_check(amount)
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()

