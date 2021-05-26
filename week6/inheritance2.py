class Product:
    def __init__(self):
        self.price = 0.0
        self.qty = 0


    def get_total_price(self):
        return self.price * self.qty


# cereal class is a child of Product and inherits the init and other methods from it
# by adding the class product in the parenthesis.
class Cereal(Product):
    def __init__(self):
        super().__init__()
        self.weight = 0.0

    def calculate_shipping_cost(self):
        return 0.05 * self.weight


corn_flakes = Cereal()
corn_flakes.price = 3.50
corn_flakes.qty = 3
corn_flakes.weight = 2.05

price = corn_flakes.get_total_price()
cost = corn_flakes.calculate_shipping_cost()
print(price)
print(cost)