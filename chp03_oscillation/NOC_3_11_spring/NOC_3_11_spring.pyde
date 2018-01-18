# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Bob
from Spring import Spring

def setup():
    size(640, 360)
    # Create objects at starting position
    # Note third argument in Spring constructor is "rest length"
    global bob, spring
    bob = Bob(width/2, 100)
    spring = Spring(width/2, 10, 100)
    
def draw():
    background(255)
    
    global bob, spring
    # Apply a gravity force to the bob
    gravity = PVector(0, 2)
    bob.applyForce(gravity)
    
    # Connect the bob to the spring (this calculates the force)
    spring.connect(bob)
    
    # Constrain spring distance between min and max
    spring.constrainLength(bob, 30, 200)
    
    # Update bob
    bob.update()
    # If it's being dragged
    bob.drag(mouseX, mouseY)
    
    # Draw everything
    spring.displayLine(bob) # Draw a line between spring and bob
    bob.display()
    spring.display()
    
    fill(0)
    text("click on bob to drag", 10, height-5)
    
# For mouse interaction with bob

def mousePressed():
    bob.clicked(mouseX, mouseY)
    
def mouseReleased():
    bob.stopDragging()