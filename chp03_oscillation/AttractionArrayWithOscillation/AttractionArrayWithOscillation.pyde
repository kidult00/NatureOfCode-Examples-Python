# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Attraction Array with Oscillating objects around each Crawler
# Click and drag attractive body to move throughout space
from Attractor import Attractor
from Crawler import Crawler


def setup():
    size(640, 360)
    
    global crawlers, a
    # Some random bodies
    crawlers = [Crawler() for i in range(6)]
    # Create an attractive body
    a = Attractor(PVector(width/2, height/2), 20, 0.4)

def draw():
    background(255)
    # global crawlers, a
    a.rollover(mouseX, mouseY)
    a.go()
    
    for each in crawlers:
        # Calculate a force exerted by "attractor" on "Crawler"
        f = a.attract(each)
        # Apply that force to the Crawler
        each.applyForce(f)
        # Update and render
        each.update()
        each.display()

def mousePressed():
    a.clicked(mouseX, mouseY)
    
def mouseReleased():
    a.stopDragging()