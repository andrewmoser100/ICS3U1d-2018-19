import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

def draw_cloud(x,y):
    """ Draw a cloud """

    arcade.draw_circle_filled(x, y + 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 70, y + 480, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 50, y + 470, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 30, y + 450, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 66, y + 520, 20, arcade.color.WHITE)

def draw_rollinghills():
    arcade.draw_circle_filled(50, 80, 300, arcade.color.GREEN)
    arcade.draw_circle_filled(200, 80, 300, arcade.color.GREEN)
    arcade.draw_circle_filled(700, 80, 300, arcade.color.GREEN)

def draw_tree(x,y, r, s):
    arcade.draw_rectangle_filled(x, y - 60, r, s, arcade.color.BROWN)
    arcade.draw_circle_filled(x, y, 100, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(x, y - 130, 20, arcade.color.DARK_BROWN)


def draw_apple(x,y):
    arcade.draw_circle_filled(x, y, 10, arcade.color.RED)
    arcade.draw_circle_filled(x + 10, y - 40, 10, arcade.color.RED)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions

    draw_cloud(300, 20)
    draw_cloud(600, 40)
    draw_cloud(100, 60)
    draw_cloud(800, 70)

    draw_rollinghills()

    draw_tree(100, 200, 50, 200)

    draw_apple(150, 200)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()