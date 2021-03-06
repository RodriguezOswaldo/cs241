"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others

This program implements an awesome version of skeet.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.ANTIQUE_RUBY
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15


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
        self.color = None
        self.alive = True

    def draw(self):
        # arcade.draw_cirdcle_outline(self.center.x, self.center.y, self.radius, self.color)
        arcade.draw_rectangle_filled(self.center.x, self.center.y, 20, 20, self.color)

    def advance(self):
        # changes the position of the object
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx

    def is_off_screen(self, width, height):
        if self.center.x > width or self.center.x < 0 or self.center.y > height or self.center.y < 0:
            return True
        else:
            return False

    def hide(self):
        self.alive = False

    def show(self):
        self.alive = True


class Bullet(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.color = BULLET_COLOR
        self.angle = 45
        self.time = 0

    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        # bullet at the tip of canon
        self.center.y = RIFLE_WIDTH * math.sin(math.radians(angle))
        self.center.x = RIFLE_WIDTH * math.cos(math.radians(angle))


class Target(FlyingObject):
    score: int = 0

    def __init__(self):
        super().__init__()

        self.center.x = random.uniform(SCREEN_WIDTH, SCREEN_WIDTH)
        self.center.y = random.uniform(SCREEN_HEIGHT/2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(-1, -3)
        self.velocity.dy = random.uniform(-1, -3)
        self.color = TARGET_COLOR
        self.radius = TARGET_RADIUS
        self.score = 0

    def draw(self):
        # arcade.draw_rectangle_filled(self.center.x - 100, self.center.y, 25, 16, arcade.color.ALABAMA_CRIMSON)
        arcade.draw_arc_outline(self.center.x - 20, self.center.y, 25, 16, arcade.color.TANGO_PINK, 60, 130)
        # arcade.draw_arc_outline(self.center.x + 40, self.center.y, 25, 16, arcade.color.CADMIUM_ORANGE, 90, 180)
        arcade.draw_circle_filled(self.center.x, self.center.y, 12, arcade.color.AQUA)

    def hit(self):
        self.set_score(1)
        self.alive = False
        return self.score

    def set_score(self, score):
        self.score = score


class SafeTarget(Target):
    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(SCREEN_WIDTH, SCREEN_WIDTH)
        self.center.y = random.uniform((SCREEN_HEIGHT/2), SCREEN_WIDTH)
        self.color = TARGET_SAFE_COLOR
        self.radius = TARGET_SAFE_RADIUS

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x - 100, self.center.y, 25, 16, arcade.color.BLACK_OLIVE)

    def hit(self):
        self.score = -10
        self.hide()
        return self.score


class StrongTarget(Target):
    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(SCREEN_WIDTH, SCREEN_WIDTH)
        self.center.y = random.uniform((SCREEN_HEIGHT/2), SCREEN_WIDTH)
        self.velocity.dx = random.uniform(-1, -2)
        self.velocity.dy = random.uniform(-1, -2)
        self.color = TARGET_SAFE_COLOR
        self.radius = TARGET_SAFE_RADIUS * 2
        self.hit_count = 0
        self.hit_intent = 3
        self.text = 3

    def draw(self):
        arcade.draw_circle_outline(self.center.x - 20, self.center.y, self.radius, arcade.color.DARK_VIOLET)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.text), text_x, text_y, arcade.color.DARK_VIOLET)

    def hit(self):
        # the strong target should move slowly
        if self.hit_count < self.hit_intent:
            self.hit_count += 1
            self.text -= 1
            self.show()
            if self.hit_count != self.hit_intent:
                self.set_score(1)
            else:
                self.set_score(5)
                self.hide()
        return self.score


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """

    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0
        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR,
                                     360 - self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []
        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        # bullets and target lists calling both draw methods
        elements = [self.bullets, self.targets]
        for element in elements:
            [item.draw() for item in element]

        # for bullet in self.bullets:
        #     bullet.draw()
        #
        # for target in self.targets:
        #     target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        targets = [
            Target(),
            SafeTarget(),
            StrongTarget()
        ]
        target_index = random.randint(0, len(targets) - 1)

        self.targets.append(
            targets[target_index]
        )

        # TODO: Decide what type of target to create and append it to the list

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                            abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.hide()
                        target.hide()
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.

        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
arcade.run()
