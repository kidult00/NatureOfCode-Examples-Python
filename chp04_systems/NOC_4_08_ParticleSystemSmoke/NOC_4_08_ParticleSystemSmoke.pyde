# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Smoke Particle System

# A basic smoke effect using a particle system
# Each particle is rendered as an alpha masked image
# /* @pjs preload="processingjs/chapter04/_4_08_ParticleSystemSmoke/data/texture.png"; */

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360)
    img = loadImage("texture.png")
    global ps
    ps = ParticleSystem(0, PVector(width / 2, height - 75), img)

def draw():
    background(0)

    # Calculate a "wind" force based on mouse horizontal position
    dx = map(mouseX, 0, width, -0.2, 0.2)
    wind = PVector(dx, 0)
    ps.applyForce(wind)
    ps.run()
    # for i in range(2): ps.addParticle()
    ps.addParticle()

    drawVector(wind, PVector(width / 2, 50, 0), 500) # Draw an arrow representing the wind force
    
# Renders a vector object 'v' as an arrow and a position 'loc'
def drawVector(v, pos, scayl):
    arrowsize = 4
    translate(pos.x, pos.y)
    stroke(255)
    # Call vector heading function to get direction (note that pointing up is a heading of 0) and rotate
    rotate(v.heading2D())
    # Calculate length of vector & scale it to be bigger or smaller if necessary
    len = v.mag() * scayl
    # Draw three lines to make an arrow (draw pointing up since we've rotate to the proper direction)
    line(0, 0, len, 0)
    line(len, 0, len-arrowsize, +arrowsize/2)
    line(len, 0, len-arrowsize, -arrowsize/2)