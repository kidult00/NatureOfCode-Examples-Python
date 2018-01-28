# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Chapter 3: Asteroids exercise

from Spaceship import Spaceship

def setup():
    size(640, 360)

    global ship
    ship = Spaceship()
    

def draw():
    background(255)
    
    ship.update()    # Update position
    ship.wrapEdges() # Wrape edges
    ship.display()   # Draw ship
    
    fill(0)
    text("left right arrows to turn, z to thrust", 10, height-5)

    # Turn or thrust the ship depending on what key is pressed
    if keyPressed :
        if key == CODED and keyCode == LEFT : ship.turn(-0.03)
        elif key == CODED and keyCode == RIGHT : ship.turn(0.03)
        elif key == 'z' or key == 'Z': ship.thrust()