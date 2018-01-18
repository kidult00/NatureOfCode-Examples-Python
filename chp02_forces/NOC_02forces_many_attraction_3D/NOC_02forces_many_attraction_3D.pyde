# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover
from Attractor import Attractor

def setup():
    size(640, 360, P3D)
    
    global movers, a, angle
    movers = [Mover(random(0.1, 2), random(-width/2, width/2), 
                    random(-height/2, height/2), random(-100,100)) for i in range(10)]
    a = Attractor()
    angle = 0.0
    
    
def draw():
    global movers, a, angle
    background(255)
    sphereDetail(8)
    lights()
    translate(width/2, height/2)
    rotateY(angle)
    
    a.display()
    
    for each in movers:
        force = a.attract(each)
        each.applyForce(force)
        each.update()
        each.display()
    angle += 0.003