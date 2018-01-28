# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Circle import Circle
from Square import Square

shapes = []

def setup():
    size(200, 200)
    global shapes
    for i in range(30):
        r = int(random(0, 2)) # r should be integer!!
        # Randomly put either circles or squares in our array
        if r == 0:
            shapes.append(Circle(100, 100, 10, color(random(255), 100)))
        else:
            shapes.append(Square(100, 100, 10))

def draw():
    background(255)
    # Jiggle and display all shapes
    for each in shapes:
        each.jiggle()
        each.display()
