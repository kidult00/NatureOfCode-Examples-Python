# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover

def setup():
    size(640, 360)
    global movers
    movers = [Mover(random(0.1, 4), 0, 0) for i in range(20)]
    
def draw():
    background(255)
    
    global movers
    wind = PVector(0.01, 0)
    gravity = PVector(0, 0.1)
    
    for each in movers :
        each.applyForce(wind)
        each.applyForce(gravity)
        
        each.update()
        each.display()
        each.checkEdges()