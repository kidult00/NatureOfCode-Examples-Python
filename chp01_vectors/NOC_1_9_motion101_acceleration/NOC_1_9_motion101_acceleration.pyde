# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover

# Example 1-2: Bouncing Ball, with PVector!
def setup():
    size(640, 360)
    global mover
    mover = Mover()

    
def draw():
    background(255)
    # Update the position
    mover.update()
    # Display the Mover
    mover.display()    