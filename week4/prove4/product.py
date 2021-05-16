class Product:
    def __init__(self, id, name, price, qy):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = qy

    def get_total_price(self):
        total_price = self.price * self.quantity
        return total_price

    def display(self):
        print(f'{self.name} ({self.quantity}) - ${round(self.get_total_price(), 2)}')


class Order:
    def __init__(self):
        self.id = ""
        self.products = []

    def get_subtotal(self):
        sub_total = 0
        for p in self.products:
            sub_total += p.get_total_price()
        return sub_total

    def get_tax(self):
        tax = self.get_subtotal() * 0.065
        return tax

    def get_total(self):
        total = self.get_tax() + self.get_subtotal()
        return total

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print(f'Order: {self.id}')
        for p in self.products:
            p.display()
        print(f'Subtotal: ${self.get_subtotal()}')
        print(f'Tax: ${round(self.get_tax(),2)}')
        print(f'Total: ${round(self.get_total(),2)}')


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

    def get_total(self):
        pass

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


def main():

    print("### Testing Products ###")
    p1 = Product("1238223", "Sword", 1899.99, 10)

    print("Id: {}".format(p1.id))
    print("Name: {}".format(p1.name))
    print("Price: {}".format(p1.price))
    print("Quantity: {}".format(p1.quantity))

    p1.display()

    print()

    p2 = Product("838ab883", "Shield", 989.75, 6)
    print("Id: {}".format(p2.id))
    print("Name: {}".format(p2.name))
    print("Price: {}".format(p2.price))
    print("Quantity: {}".format(p2.quantity))

    p2.display()

    print("\n### Testing Orders ###")
    # Now test Orders
    order1 = Order()
    order1.id = "1138"
    order1.add_product(p1)
    order1.add_product(p2)

    order1.display_receipt()

    print("\n### Testing Customers ###")
    # Now test customers
    c = Customer()
    c.id = "aa32"
    c.name = "Gandalf"
    c.add_order(order1)

    c.display_summary()

    print()
    c.display_receipts()

    # Add another product and order and display again

    p3 = Product("2387127", "The Ring", 1000000, 1)
    p4 = Product("1828191", "Wizard Staff", 199.99, 3)

    order2 = Order()
    order2.id = "1277182"
    order2.add_product(p3)
    order2.add_product(p4)

    c.add_order(order2)

    print()
    c.display_summary()

    print()
    c.display_receipts()


if __name__ == "__main__":
    main()
