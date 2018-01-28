# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360)
    global ps
    ps = ParticleSystem(PVector(width / 2, 50))

def draw():
    background(255)

    ps.addParticle()
    ps.run()