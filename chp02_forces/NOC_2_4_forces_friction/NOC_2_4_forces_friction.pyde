# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover

def setup():
    size(383, 200)
    randomSeed(1)
    global movers
    movers = [Mover(random(1, 4), random(width), 0) for i in range(5)]
    
def draw():
    background(255)
    
    global movers
    wind = PVector(0.01, 0)
    
    for each in movers :
        c = 0.05
        gravity = PVector(0, 0.1 * each.mass)
        friction = each.velocity.get()
        friction.mult(-1)
        friction.normalize()
        friction.mult(c)
        
        each.applyForce(friction)
        each.applyForce(wind)
        each.applyForce(gravity)
        
        each.update()
        each.display()
        each.checkEdges()