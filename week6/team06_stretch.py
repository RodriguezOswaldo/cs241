class Point:
    def __init__(self):
        self.x = 0.00
        self.y = 0.00

    def prompt_for_point(self):
        self.x = int(input('Enter x: '))
        self.y = int(input('Enter y: '))

    def display(self):
        print('\nCenter:')
        print(f'({self.x}, {self.y})')


class Circle:
    def __init__(self):
        super().__init__()
        self.radius = 0
        self.center = Point()

    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = int(input('Enter radius: '))

    def display(self):
        Point.display(self)
        print(f'Radius: {self.radius}')


print('\nNext')
print('-----')
my_circle = Circle()
my_circle.prompt_for_circle()
my_circle.display()
