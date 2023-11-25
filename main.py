from p5 import *

# window size
window_width = 1200
window_height = 800


def setup():
    size(window_width, window_height)
    title("LAB-IMFJV-1 - Aluno: Steven Hall 22001753")

    """ Function that draws a car
    """

def draw_car():

    fill(255, 0, 0)
    #Roof
    line((500, 700), (700, 700))

    #Botton
    line((500, 600), (700, 600))

    noFill()
    begin_shape()
    arc((400, 500), 200, -200, 0, PI)
    end_shape()

    # TODO : windows

    # TODO : Wheels




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

def draw():
    background(50)
    #box(70,170,70)
    draw_buildings()
    draw_car()








run()