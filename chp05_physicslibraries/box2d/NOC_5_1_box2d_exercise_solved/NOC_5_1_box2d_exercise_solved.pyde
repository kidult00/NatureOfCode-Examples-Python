# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

add_library('box2d_processing')
# add_library('jbox2d')

from Box import Box

def setup():
    size(640, 360)
    global box2d, boxes
    box2d = Box2DProcessing(this)
    box2d.createWorld()
    boxes = []
    
def draw():
    background(255)

    box2d.step()
    
    # When the mouse is clicked, add a new Box object
    if mousePressed :
        p = Box(mouseX, mouseY)
        boxes.append(p)
        
    # Display all the boxes
    for b in boxes: b.display()