from order import Order


class Product:
    def __init__(self, id, name, price, qy):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = qy

    def get_total_price(self):
        return self.quantity * self.price

    def display(self):
        txt = "{} ({}) - ${:.2f}"
        print(txt.format(self.name, self.quantity, self.get_total_price()))
        # print(f'{self.name} ({self.quantity}) - ${self.get_total_price()}')

