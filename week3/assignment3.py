class Robot:

    def __init__(self):
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel_amount = 100

    def move_left(self):
        # Left should subtract one from the x-coordinate
        if self.fuel_amount <= 0:
            print('Insufficient fuel to perform action')
        else:
            self.fuel_amount -= 5
            self.x_coordinate -= 1
        return

    def move_right(self):
        # Right should add one from the x-coordinate
        if self.fuel_amount <= 0:
            print('Insufficient fuel to perform action')
        else:
            self.fuel_amount -= 5
            self.x_coordinate += 1
        return

    def move_down(self):
        # Down should add 1 to the y-coordinate,
        if self.fuel_amount <= 0:
            print('Insufficient fuel to perform action')
        else:
            # When told to move, the robot's fuel should decrease by 5,
            self.fuel_amount -= 5
            self.y_coordinate += 1
        return

    def move_up(self):
        # Up should subtract 1 to the y-coordinate,
        if self.fuel_amount <= 0:
            print('Insufficient fuel to perform action')
        else:
            # When told to move, the robot's fuel should decrease by 5,
            self.fuel_amount -= 5
            self.y_coordinate -= 1
        return

    def status(self):
        return print(f'{self.x_coordinate} , {self.y_coordinate} - {self.fuel_amount}')

    def fire_laser(self):
        if self.fuel_amount <= 0:
            print('Insufficient fuel to perform action')
        else:
            print("Pew! Pew!")
            self.fuel_amount -= 15
        return self.fuel_amount


# def interact_with_robot():

    message = ''
    while message != 'quit':
        message == input('Give the robot a command: ')


# interact_with_robot()
my_robot = Robot()
mine = my_robot.fire_laser()
fuel = my_robot.fuel_amount
print(mine)