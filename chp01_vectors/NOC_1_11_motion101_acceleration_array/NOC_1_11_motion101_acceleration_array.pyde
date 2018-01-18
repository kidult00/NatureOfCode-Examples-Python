# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Demonstration of the basics of motion with vector.
# A "Mover" object stores position, velocity, and acceleration as vectors
# The motion is controlled by affecting the acceleration (in this case towards the mouse)

from Mover import Mover

def setup():
    size(640, 360)
    global movers
    movers = [Mover() for i in range(20)]

    
def draw():
    background(255)
    for i in range(20):
        # Update the position
        movers[i].update()
        # Display the Mover
        movers[i].display()    