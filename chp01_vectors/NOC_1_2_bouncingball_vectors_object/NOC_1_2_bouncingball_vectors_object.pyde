# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Ball import Ball

# Example 1-2: Bouncing Ball, with PVector!
def setup():
    size(200, 200)
    global b
    b = Ball()

    
def draw():
    background(255)
    b.update()
    b.display()    