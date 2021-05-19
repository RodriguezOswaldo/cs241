import arcade

WIDTH = 600
HEIGHT = 600
TITLE = "Hello World from Arcade"
RADIUS = 140

# open the window
arcade.open_window(WIDTH, HEIGHT, TITLE)

# set background color
arcade.set_background_color(arcade.color.AQUA)

# clear the screen and start drawing
arcade.start_render()

# Draw a circle
arcade.draw_circle_filled(
    WIDTH/2, HEIGHT/2, RADIUS, arcade.color.CORN
)

# Finish Draw
arcade.finish_render()

# Display Everything
arcade.display()

