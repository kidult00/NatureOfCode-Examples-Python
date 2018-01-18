# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Walker import Walker

def setup():
    size(600, 400)
    # frameRate(10)
    global w
    # Creat a walker object
    w = Walker()
    background(255)

def draw():
    # Run the wlker object
    w.step()
    w.render()