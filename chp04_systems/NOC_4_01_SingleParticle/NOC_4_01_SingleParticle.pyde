# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

def setup():
    size(640, 360)
    background(255)
    smooth()
    global p
    p = Particle(PVector(width/2, 20))
    
def draw():
    background(255)
    global p
    p.run()
    if p.isDead() :
        p = Particle(PVector(width/2, 20))