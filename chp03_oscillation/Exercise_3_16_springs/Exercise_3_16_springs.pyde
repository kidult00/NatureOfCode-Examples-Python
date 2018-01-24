# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Bob
from Spring import Spring

def setup():
    size(640, 360)
    # Create objects at starting position
    # Note third argument in Spring constructor is "rest length"
    global b1, b2, b3, s1, s2, s3
    b1 = Bob(width/2, 100)
    b2 = Bob(width/2, 200)
    b3 = Bob(width/2, 300)
    s1 = Spring(b1, b2, 100)
    s2 = Spring(b2, b3, 100)
    s3 = Spring(b1, b3, 100)
    
def draw():
    background(255)
    
    s1.update()
    s2.update()
    s3.update()
    
    s1.display()
    s2.display()
    s3.display()
    
    b1.update()
    b1.display()
    b2.update()
    b2.display()
    b3.update()
    b3.display()
    
    b1.drag(mouseX, mouseY)

def mousePressed():
    b1.clicked(mouseX, mouseY)
    
def mouseReleased():
    b1.stopDragging()