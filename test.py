from p5 import *

angle = 0


def setup():
    size(800, 600)
    no_fill()

def draw():
    background(240)
    translate(400, 300) # move the origin to the mouse position
    angle = p5.frame_count * 0.01 # calculate the angle based on the frame count
    for i in range(12): # draw 12 lines
        rotate(angle + i * PI / 6) # rotate each line by a different angle
        stroke(0, 0, 255) # set the stroke color to blue
        line(0, 0, 100, 0) # draw a line from the origin to (100, 0)

run()