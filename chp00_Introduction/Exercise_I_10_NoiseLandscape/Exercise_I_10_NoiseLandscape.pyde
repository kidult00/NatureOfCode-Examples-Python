# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Landscape with height values according to Perlin noise

from Landscape import Landscape

def setup():
    size(800, 200, P3D)
    
    global land, theta
    # Create a landscape object
    land = Landscape(20, 800, 400)
    theta = 0.0


def draw():
    global land, theta
    # Visualize the landscape space
    background(255)
    pushMatrix()
    translate(width/2, height/2+20, -160)
    rotateX(PI/3)
    rotateZ(theta)
    land.render()
    popMatrix()
    
    land.calculate()
    
    theta += 0.0025