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


