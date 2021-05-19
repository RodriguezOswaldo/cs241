import arcade
import pymunk

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class Box:
    def __init__(self):
        self.x = 100
        self.y = 100

        self.dx = 1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, 50, 20, arcade.color.AIR_FORCE_BLUE)

    def advance(self):
        if self.x > SCREEN_WIDTH:
            self.dx = -1
        elif self.x < 0:
            self.dx = 1

        self.x += self.dx


class DemoApp(arcade.Window):
    """
    Defining the demo application
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.CORN)

        self.box = Box()

    def on_draw(self):
        """
        Called everytime we need to draw the window
        :return:
        """
        arcade.start_render()
        self.box.draw()

    def update(self, delta_time: float):
        self.box.advance()


window = DemoApp(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
