# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Demonstration of normalizing a vector.
# Normalizing a vector sets its length to 1.

def setup():
    size(640, 360)
    
def draw():
    background(255)
    # A vector that points to the mouse position
    mouse = PVector(mouseX, mouseY)
    # A vector that points to the center of the window
    center = PVector(width/2, height/2)
    # Subtract center from mouse which results in a vector that points from center to mouse
    mouse.sub(center)
    
    # Normalize the vector
    mouse.normalize();
    
    # Multiply its length by 50
    mouse.mult(150)
    
    translate(width/2, height/2)
    # Draw the resulting vector
    strokeWeight(2)
    stroke(0)
    line(0, 0, mouse.x, mouse.y)