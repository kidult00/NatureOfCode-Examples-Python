# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from ParticleSystem import ParticleSystem
from Repeller import Repeller

def setup():
    size(640, 360)
    global ps, repeller
    ps = ParticleSystem(PVector(width / 2, 50))
    repeller = Repeller(width / 2 - 20, height / 2)

def draw():
    background(255)
    ps.addParticle()
    # Apply gravity force to all Particles
    gravity = PVector(0, 0.1)
    ps.applyForce(gravity)
    ps.applyRepeller(repeller)
    
    repeller.display()
    ps.run()
