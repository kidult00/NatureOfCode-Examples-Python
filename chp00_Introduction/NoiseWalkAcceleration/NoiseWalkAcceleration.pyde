# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Walker import Walker

def setup():
    size(640, 360)
    
    global w
    # Create a walker object
    w = Walker()

def draw():
    background(255)
    # Run the walker object
    w.walk()
    w.display()