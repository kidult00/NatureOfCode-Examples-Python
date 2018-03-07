# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Box import Box

def setup():
    size(640, 360)
    global boxes
    boxes = []
    
def draw():
    background(255)

    # When the mouse is clicked, add a new Box object
    if mousePressed :
        p = Box(mouseX, mouseY)
        boxes.append(p)
        
    # Display all the boxes
    for b in boxes: b.display()