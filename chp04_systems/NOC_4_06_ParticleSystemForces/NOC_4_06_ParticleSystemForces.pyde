# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360)
    global ps
    ps = ParticleSystem(PVector(width / 2, 50))

def draw():
    background(255)

    # Apply gravity force to all Particles
    gravity = PVector(0, 0.1)
    ps.applyForce(gravity)
    ps.addParticle()
    ps.run()
