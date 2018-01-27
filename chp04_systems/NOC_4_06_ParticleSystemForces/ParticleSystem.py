# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)
from Particle import Particle

# Simple Particle System

class ParticleSystem(object):

    def __init__(self, position):
        self.particles = []  
        self.origin = position      
        
    def applyForce(self, f):
        for each in self.particles: each.applyForce(f)

    def addParticle(self):
        self.particles.append(Particle(self.origin))
        
    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)