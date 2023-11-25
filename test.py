""" Test code for 3D CAR
from p5 import *

car_position = Vector(100, 300, 0)

def setup():
    size(800, 600)  # Use P3D for 3D rendering
    no_stroke()

def draw():
    background(200)
    # Car body
    with push_matrix():
        translate(car_position.x, car_position.y, car_position.z)
        fill(255, 0, 0)
        box(150, 60, 30)

    # Car roof
    with push_matrix():
        #translate(car_position.x, car_position.y - 30, car_position.z)
        fill(0, 0, 255)
        box(120, 30, 30)

    # Wheels
    wheel_radius = 20

    with push_matrix():
        translate(car_position.x - 50, car_position.y + 30, car_position.z + 15)
        fill(0)
        cylinder(wheel_radius, 10)

    with push_matrix():
        translate(car_position.x + 50, car_position.y + 30, car_position.z + 15)
        fill(0)
        cylinder(wheel_radius, 10)

    # Move the car
    #car_position.x += 2

run(mode='P3D')
"""