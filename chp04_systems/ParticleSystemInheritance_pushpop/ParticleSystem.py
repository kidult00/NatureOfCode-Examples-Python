# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from ParticleChild import ParticleChild
from Particle import Particle

class ParticleSystem(object):

    def __init__(self, position):
        self.particles = []
        self.origin = position.get()

    def addParticle(self):
        r = random(1)
        if r < 0.5:
            self.particles.append(Particle(self.origin))
        else:
            self.particles.append(ParticleChild(self.origin))

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)
