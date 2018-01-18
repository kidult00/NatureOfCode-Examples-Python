# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover
from Attractor import Attractor

def setup():
    size(640, 360)
    global m, a
    m = Mover()
    a = Attractor()
    
    
def draw():
    background(255)
    
    global m, a
    force = a.attract(m)
    m.applyForce(force)
    m.update()
    
    a.drag()
    a.hover(mouseX, mouseY)
    
    a.display()
    m.display()
    m.checkEdges()
    

def mousePressed():
    a.clicked(mouseX, mouseY)
    
def mouseReleased():
    a.stopDragging()