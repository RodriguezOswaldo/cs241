class Product:
    def __init__(self):
        self.ID = None
        self.name = ''
        self.Price = None
        self.Quantity = None

    def get_total_price(self):
        total_price = self.Price * self.Quantity
        return total_price

    def display(self):
        print(f'{self.get_total_price()}')


new_product = Product()
one = new_product.name = input('Name: ')
two = new_product.Price = float(input('Price: '))
three = new_product.Quantity = int(input('Quantity: '))
four = new_product.ID = input('ID: ')

new_product.display()
