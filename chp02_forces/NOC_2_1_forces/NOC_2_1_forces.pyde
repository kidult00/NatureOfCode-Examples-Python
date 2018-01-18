# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover

def setup():
    size(640, 360)
    global m
    m = Mover()
    
def draw():
    background(255)
    global m
    wind = PVector(0.01, 0)
    gravity = PVector(0, 0.1)
    m.applyForce(wind)
    m.applyForce(gravity)
    
    m.update()
    m.display()
    m.checkEdges()