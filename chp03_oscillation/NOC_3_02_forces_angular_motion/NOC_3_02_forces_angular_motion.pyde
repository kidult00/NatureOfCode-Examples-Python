# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover
from Attractor import Attractor

def setup():
    size(640, 360)
    global movers, a
    movers = [Mover(random(0.1, 2), random(width), random(height)) for i in range(20)]
    a = Attractor()
    
    
def draw():
    background(255)
    global movers, a
    a.display()
    
    for each in movers:
        force = a.attract(each)
        each.applyForce(force)
        each.update()
        each.display()
    