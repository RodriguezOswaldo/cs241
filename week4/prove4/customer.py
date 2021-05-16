from product import Product
from order import Order


class Customer:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.orders = []

    def get_order_count(self):
        order_count = 0
        for my_order in self.orders:
            order_count += my_order
        return order_count

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        total_order = 0
        add = 0
        for order in self.orders:
            total_order += order.get_total()
            add += 1

        print(f'Summary for customer \'{self.id}\'')
        print(f'Name: {self.name}')
        print(f'Order: {add}')
        print(f'Total: ${round(total_order,2)}')

    def display_receipts(self):
        print(f'Detailed receipts for customer \'{self.id}\':')
        print(f'Name: {self.name}')
        print()

        for o in self.orders:
            o.display_receipt()
            print()

