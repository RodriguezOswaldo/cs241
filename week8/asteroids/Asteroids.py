"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others

This program implements the asteroids game.
"""
import math
import random
import arcade

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class Velocity:
    def __init__(self):
        self.dx = 0
        self.dy = 0


class FlyingObject:
    def __init__(self):
        # object location is Point()
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0

    def draw(self):
        pass

    def advance(self):
        # changes the position of the object
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx


class Bullet(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.angle = 45
        self.time = 0

    def fire(self, angle):
        pass


class Asteroid(FlyingObject):
    """
    Asteroid Base Class
    """
    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(SCREEN_WIDTH, SCREEN_WIDTH)
        self.center.y = random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(-1, -3)
        self.velocity.dy = random.uniform(-1, -3)

    def draw(self):
        pass


class BigRock(Asteroid):
    """
    Big Asteroid
    """
    def __init__(self):
        super().__init__()

    def draw(self):
        img = "images/meteorGrey_big1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        # width = 340
        # height = 349
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        # arcade.draw_rectangle_filled(x, y, width, height, color=arcade.color.NAVY_BLUE)
        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)


class MediumRock(Asteroid):
    """
       Medium Asteroid
       """
    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(SCREEN_WIDTH, SCREEN_WIDTH)
        self.center.y = random.uniform((SCREEN_HEIGHT / 2), SCREEN_WIDTH)

    def draw(self):
        img = 'images/meteorGrey_med1.png'
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        # width = 340
        # height = 349
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)


class SmallRock(Asteroid):
    """
    Small Asteroid
    """
    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(SCREEN_WIDTH, SCREEN_WIDTH)
        self.center.y = random.uniform((SCREEN_HEIGHT / 2), SCREEN_WIDTH)

    def draw(self):
        img = "images/meteorGrey_small1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)


class Ship(FlyingObject):
    """
    Ship
    """
    def __init__(self):
        super().__init__()
        pass


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()
        self.asteroids = []

        # TODO: declare anything here you need the game class to track
        self.asteroid = BigRock()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        # self.create_target()
        self.asteroid.draw()
        # for asteroid in self.asteroid:


    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        # decide if we should start a target

        self.asteroid.advance()
        # TODO: Check for collisions

    # def create_asteroids(self):
    #     asteroids = [
    #         BigRock()
    #     ]
    #     # asteroid_index = random.randint(0, len(asteroids) - 1)
    #     asteroid_index = random.randint(0, 4)
    #
    #     self.asteroids.append(
    #         asteroids[asteroid_index]
    #     )
    #     pass


    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
