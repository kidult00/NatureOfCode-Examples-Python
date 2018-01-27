# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

def setup():
    size(800, 200)
    background(255)
    smooth()
    global p
    p = Particle(PVector(width / 2, 20))

def draw():
    if mousePressed:
        noStroke()
        fill(255, 5)
        rect(0, 0, width, height)
        p.run()
        if p.isDead():
            print('Particle dea!')
