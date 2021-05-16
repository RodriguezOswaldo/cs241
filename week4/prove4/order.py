
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
        return self.get_subtotal() * 0.065

    def get_total(self):
        return self.get_tax() + self.get_subtotal()

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print(f'Order: {self.id}')
        for p in self.products:
            p.display()
        print(f'Subtotal: ${self.get_subtotal()}')
        print(f'Tax: ${round(self.get_tax(),2)}')
        print(f'Total: ${round(self.get_total(),2)}')


