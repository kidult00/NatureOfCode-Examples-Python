# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Walker import Walker

def setup():
    size(640, 360)
    background(0)
    
    global w
    # Creat a walker object
    w = Walker()


def draw():
    # Run the wlker object
    w.step()
    w.render()