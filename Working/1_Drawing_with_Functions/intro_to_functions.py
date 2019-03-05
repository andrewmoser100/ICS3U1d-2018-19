import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

def draw_cloud():
    """ Draw a cloud """
    arcade.draw_circle_filled(300, 500, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 580, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(260, 540, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(360, 540, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(360, 520, 40, arcade.color.WHITE)

    arcade.draw_circle_filled(660, 540, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(630, 540, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(660, 490, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(620, 510, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(670, 500, 40, arcade.color.WHITE)

def draw_rollinghills():
    arcade.draw_circle_filled(50, 80, 300, arcade.color.GREEN)
    arcade.draw_circle_filled(200, 80, 300, arcade.color.GREEN)
    arcade.draw_circle_filled(700, 80, 300, arcade.color.GREEN)

def draw_tree():
    arcade.draw_circle_filled(200, 200, 100, arcade.color.DARK_GREEN)
    arcade.draw_rectangle_filled(200, 10, 50, 300, arcade.color.BROWN)
    arcade.draw_circle_filled(200, 100, 20, arcade.color.DARK_BROWN)

def draw_apple():
    arcade.draw_circle_filled(150, 200, 10, arcade.color.RED)
    arcade.draw_circle_filled(250, 240, 10, arcade.color.RED)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_rollinghills()
    draw_tree()
    draw_apple()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()