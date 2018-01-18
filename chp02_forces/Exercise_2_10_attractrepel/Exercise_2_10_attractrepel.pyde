# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover
from Attractor import Attractor

def setup():
    size(640, 360)
    global movers, a
    movers = [Mover(random(4, 12), random(width), random(height)) for i in range(20)]
    a = Attractor()
    
    
def draw():
    background(255)
    global movers, a
    a.display()
    a.drag()
    a.hover(mouseX, mouseY)
    
    
    for i in range(len(movers)):
        for j in range(len(movers)):
            if i != j:
                force = movers[j].repel(movers[i])
                movers[i].applyForce(force)
        
        force = a.attract(movers[i])
        movers[i].applyForce(force)
        movers[i].update()
        movers[i].display()
    

def mousePressed():
    a.clicked(mouseX, mouseY)
    
def mouseReleased():
    a.stopDragging()
    
    