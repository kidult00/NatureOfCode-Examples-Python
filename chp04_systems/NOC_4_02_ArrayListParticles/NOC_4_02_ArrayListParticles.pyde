# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

particles = []

def setup():
    size(640, 360) 
    

def draw():
    background(255)

    particles.append(Particle(PVector(width / 2, 50)))
    # Looping through backwards to delete
    for i, p in enumerate(particles):
        p.run()
        if p.isDead(): particles.pop(i)
