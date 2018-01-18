# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Walker import Walker

def setup():
    size(400, 400)
    frameRate(30)
    
    global w
    # Creat a walker object
    w = Walker()


def draw():
    background(255)
    # Run the wlker object
    w.walk()
    w.display()