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
            print("Insufficient fuel to perform action")
        else:
            # When told to move, the robot's fuel should decrease by 5,
            self.fuel_amount -= 5
            self.y_coordinate += 1
        return

    def move_up(self):
        # Up should subtract 1 to the y-coordinate,
        if self.fuel_amount <= 0:
            print("Insufficient fuel to perform action")
        else:
            # When told to move, the robot's fuel should decrease by 5,
            self.fuel_amount -= 5
            self.y_coordinate -= 1
        return

    def status(self):
         print(f'({self.x_coordinate}, {self.y_coordinate}) - Fuel: {self.fuel_amount}')
         return

    def fire_laser(self):
        if self.fuel_amount <= 0:
            print("Insufficient fuel to perform action")
        else:
            print("Pew! Pew!")
            self.fuel_amount -= 15
        return


def main():

    new_robot = Robot()
    message = ""
    while message != "quit":

        message = input("Enter command: ")
        # check what is in command to perform specific action
        if message == "left":
            new_robot.move_left()
        elif message == "right":
            new_robot.move_right()
        elif message == "up":
            new_robot.move_up()
        elif message == "down":
            new_robot.move_down()
        elif message == "fire":
            new_robot.fire_laser()
        elif message == "status":
            new_robot.status()
        elif message == "quit":
            print("Goodbye.")



if __name__ == "__main__":
    main()
