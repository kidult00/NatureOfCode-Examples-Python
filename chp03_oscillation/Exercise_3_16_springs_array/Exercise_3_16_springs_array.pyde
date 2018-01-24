# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Bob
from Spring import Spring

def setup():
    size(640, 360)
    # Create objects at starting position
    # Note third argument in Spring constructor is "rest length"
    global bobs, springs
    bobs = [Bob(width/2, i*40) for i in range(5)]
    springs = [Spring(bobs[i], bobs[i+1], 40) for i in range(4)] 
    
def draw():
    background(255)
    
    for each in springs:
        each.update()
        each.display()
    
    for each in bobs:
        each.update()
        each.display()
        each.drag(mouseX, mouseY)

def mousePressed():
    for each in bobs:
        each.clicked(mouseX, mouseY)
    
def mouseReleased():
    for each in bobs:
        each.stopDragging()