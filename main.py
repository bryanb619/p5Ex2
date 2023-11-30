"""
    LAB-IMFJV-1 - Author: Steven Hall
    Simple program that draws xxx objects on the screen
    using the p5 library.

    References:

    p5 ---->
        - doc: https://p5.readthedocs.io/en/latest/tutorials/2D%20transformations.html
        - rotations: https://p5.readthedocs.io/en/latest/tutorials/2D%20transformations.html#rotation
        - push & pop: https://p5.readthedocs.io/en/latest/tutorials/2D%20transformations.html#push-and-pop
    
    art ---->
        - car: https://assetstore.unity.com/packages/tools/physics/2d-car-73763
"""

from p5 import *


class Building:
    def __init__(self,buildingSize_x, buildingSize_y):
        self.buildingSize_x = buildingSize_x; 
        self.buildingSize_y = buildingSize_y;




""" Window Settings """ 
window_width = 1200
window_height = 800
window_title = "LAB-IMFJV-1 - Aluno: Steven Hall 22001753"
frame_count = 0 
# Rotation angle 
ang = 0


""" Car Settings """ 
# Car position X
car_x = 300  

# Car position Y
car_y = 600 

# Car width
car_width = 460

# collumn width
collumn_width = 10
cullumn_center_width = 15


# Arc Settings
# left arc
left_arc_x = 450
# right arc
right_arc_x = 650


# common arc settings
arc_y = 700
arc_width = 80
arc_height = -80
# -----------------------------

""" Buildings Settings """
""" Background Settings """
""" Windmill Settings """
mill_angle = 0



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
    # TODO : Discover something better than a rect, maybe an elipse
    pass
# --------------------------------------------------------

""" Function that draws a car

    1. Draws the body
    2. Draws the windows
"""
def draw_car_body():

    # car color
    fill(254, 232, 0)

    # no outline (removes outline)
    no_stroke()

    # main body
    rect((car_x, car_y), car_width, 100)

    # back collumn
    with push_matrix():
        # center rect at 350, 450
        translate(350, 550)
        # rotate rect 20 degrees
        rotate(radians(20))
        rect((0, 0), collumn_width, 80)
        # -----------------------------

    # middle collumn
    rect((490, 515), cullumn_center_width, 90)

    # top collumn
    rect((370,515),200 ,10)

    # front collumn
    with push_matrix():
        # center rect at 550, 400
        translate(565, 520)
        # rotate rect -40 degrees
        rotate(radians(-40))
        rect((0, 0), collumn_width, 120)
        # -----------------------------

    stroke(0,0,0)
    # car details
    line((530,650),(530,600))
    #line((530,650),(530,600))

    # TODO : car windows

# --------------------------------------------------------

"""Function that draws the car wheels
"""
def draw_car_wheels():

    global ang

    # stroke collor
    stroke(0, 0, 0)

    # arc collor
    fill(48, 48, 48)

    # Left arc
    arc((left_arc_x, arc_y), arc_width, arc_height, 0, PI)

    # Right Arc
    arc((right_arc_x, arc_y), arc_width, arc_height, 0, PI)

    # TODO : Wheels
    fill(60, 72, 60)

    # Left wheel
    fill(70,70,70)
    circle((left_arc_x, arc_y), 30)

    # Right wheel
    circle((right_arc_x, arc_y), 30)


    
    with push_matrix():
        no_fill()
        stroke(0, 0, 0)
        translate(left_arc_x, arc_y)
        rotate(radians(ang))
        circle((0,0), 50)
        ang += 1
        # -----------------------------


    with push_matrix():
        no_fill()
        stroke(0, 0, 0)
        stroke_weight(2)
        translate(right_arc_x, arc_y)
        rotate(radians(ang))
        circle((0,0), 50)
        ang += 1
        # -----------------------------

    #fill(0,0,0)
    #circle((left_arc_x,arc_y),40)

    # TODO : Tires


# --------------------------------------------------------

""" Function that draws a building

    :param pos_x: building position X
    :param pos_y: building position Y
    :param width: building width
    :param height: building height

    1. Draws the main building with givem parameters
    2. Draws the windows
    3. Uses a for loop until 9 windows are complete
    4. width and height are divided by 10 = to get always the same size windows  and transform
    5. windows also use pos_x and pos_y to be drawn
    6. For loop uses i to increment the position of the windows
    7. i is multiplied by a value to increment the position of the windows
    8. heightAddValue is used to increment the position of the windows in the Y axis (lower in the canvas)
    9. multValue is used to increment the position of the windows in the X axis (right in the canvas)~
    10. rect is applyed to draw the windows using the values calculated in the for loop

    Called functions:
        - change_window_values()

"""
def draw_building(pos_x = 0, pos_y = 0, width = 100, height = 200):

    heightAddValue = 0
    multValue = 0
    windowIncrement = 1
 
    fill(118, 123, 126)
    rect((pos_x, pos_y), width, height)


    for windowIncrement in range(0, 9):
        fill(100, 100, 100)

        rect((pos_x + 10 / pos_x + (windowIncrement * multValue), pos_y + heightAddValue), width/10, height/10)
        #change_window_values()
        # --------------------------------------------------------------------


def change_window_values():

        global heightAddValue, multValue, windowIncrement
    

        if windowIncrement == 0:
            heightAddValue += 10
            multValue = 10

        elif windowIncrement == 3:
            heightAddValue += 30
            multValue = 20
        
        elif windowIncrement == 6:
            heightAddValue += 60
            multValue = 30

        windowIncrement += 1



"""function draws moutains

"""
def draw_background(pos_x_1, pos_y_1,pos_x_2, pos_y_2):
    # TODO : * Mountains *
    # TODO : Receive line position as parameter
    line((pos_x_1, pos_y_1), (pos_x_2, pos_y_2))
# --------------------------------------------------------


"""Function draws a windmill
    1.
    2.
    3.
    4.
"""
def windmill():
    # TODO : Draw windmill
    rect ((700),(200),10,20)
    triangle((700,200),(700,220),(710,210)) # CONFIGURAR TRIANGULO

    #for i in range(0,4):

        # line 
        # line((700,200),(700,220)) # CONFIGURAR LINHA

        #with push_matrix():
           # global ang
            #rect((700,200),10,20) # CONFIGURAR RETANGULO
            # aplicar rotação CORRETA   https://p5.readthedocs.io/en/latest/tutorials/2D%20transformations.html#rotation
            # ang += 1
            # -----------------------------

# --------------------------------------------------------

    """ Draw function
        1. background
        2. buildings
        3. car
        4. street
    """

def draw():
    
    background(72)

    # BACKGROUND => MOUNTAINS
    draw_background(300,200, 400, 300)

    # Windmill
    windmill()

    # STREET
    street()

    # BUILDINGS
    draw_building(300, 200, 50, 80)

    draw_car_body()
    draw_car_wheels()
      
      
run()