
class Order:
    def __init__(self):
        self.id = ""
        self.products = []

    # I converted this in a list comprehension below with the same function name.
    # def get_subtotal(self):
    #     sub_total = 0
    #     for p in self.products:
    #         sub_total += p.get_total_price()
    #     return sub_total

    def get_subtotal(self):
        return sum(p.get_total_price() for p in self.products)

    def get_tax(self):
        return 0.065 * self.get_subtotal()

    def get_total(self):
        return self.get_tax() + self.get_subtotal()

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print(f'Order: {self.id}')
        for p in self.products:
            p.display()
        txt = "Subtotal: ${:.2f}"
        print(txt.format(self.get_subtotal()))
        taxes_txt = "Tax: ${:.2f}"
        print(taxes_txt.format(self.get_tax()))
        total_txt = "Total: ${:.2f}"
        print(total_txt.format(self.get_total()))
