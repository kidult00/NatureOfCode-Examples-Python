# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover

def setup():
    size(640, 360)
    global movers
    movers = [Mover(random(0.1, 2), random(width), random(height)) for i in range(20)]
    
    
def draw():
    background(255)
    global movers
    
    for i in range(len(movers)):
        for j in range(len(movers)):
            if i != j :
                force = movers[j].attract(movers[i])
                movers[i].applyForce(force)
        movers[i].boundaies()
        movers[i].update()
        movers[i].display()
    