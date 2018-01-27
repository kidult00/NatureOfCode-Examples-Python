# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)
from Particle import Particle

# Using Generics now!  comment and annotate, etc.

class ParticleSystem(object):

    def __init__(self, position):
        self.particles = []
        self.origin = position

    def addParticle(self):
        self.particles.append(Particle(self.origin))

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)
