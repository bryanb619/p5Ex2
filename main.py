"""
    LAB-IMFJV-1 - Author: Steven Hall
    Simple program that draws xxx objects on the screen
    using the p5 library.

"""

from p5 import *

""" Window Settings """ 
window_width = 1200
window_height = 800
window_title = "LAB-IMFJV-1 - Aluno: Steven Hall 22001753"
frame_count = 0 


""" Car Settings """ 
# Car position X
car_x = 300  

# Car position Y
car_y = 600 

# Car width
car_width = 460

# Arc Settings

# Buildings

# Windmill



""" Function that sets up the window
    1. Sets the size
    2. Sets the title
"""
def setup():
    size(window_width, window_height)
    title(window_title)


# --------------------------------------------------------

def street():
    #fill(48, 40,40)
    #rect((300, 700), 100, 100)
    pass
# --------------------------------------------------------

""" Function that draws a car

    1. Draws the body
    2. Draws the windows
"""
def draw_car_body():

    # car color
    fill(254, 232, 0)

    # no outline
    no_stroke()

    # main body
    rect((car_x, car_y), car_width, 100)


    # back collumn
    with push_matrix():
        # center rect at 350, 450
        translate(350, 450)
        rotate(radians(20))
        rect((0, 0), 25, 50)

    # middle collumn
    rect((500, 370), 20, 100)

    # front collumn
    with push_matrix():
        # center rect at 550, 400
        translate(565, 500)
        # rotate -40
        rotate(radians(-40))

        rect((0, 0), 10, 120)

    # TODO : windows

# --------------------------------------------------------

"""Function that draws the car wheels
"""
def draw_car_wheels():
    #noFill()

    # Left Arc
    stroke(0, 0, 0)

    fill(48, 48, 48)
    arc((400, 700), 80, -80, 0, PI)
 
    fill(0, 0, 0)
    rotate(radians(frame_count * 6))
    circle((400, 700), 50)

    # TODO : Wheels
    

    # TODO : Tires


# --------------------------------------------------------

""" Function that draws the buildings
"""
def draw_buildings():
    fill(0, 255, 0)
    rect((200, 200), 100, 100)

    # TODO : Draw more buildings

    # TODO : Smaller buildings (require position parameters)

    # TODO : Draw Windows


def background_():

    # TODO : Mountains

    # TODO : Draw windmill
    pass

# --------------------------------------------------------

    """ Draw function
        1. Sets background color
        2. Draws street
        3. Draws car
        4. Draws buildings
        5. Draws background
    """
def draw():
    
    background(72)

    street()
    draw_buildings()
    draw_car_body()
    draw_car_wheels()
    
    
    
    








run()