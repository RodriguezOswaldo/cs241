from order import Order


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

