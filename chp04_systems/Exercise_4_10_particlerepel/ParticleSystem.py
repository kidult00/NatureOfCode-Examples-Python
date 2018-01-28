# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleSystem(object):

    def __init__(self, position):
        self.particles = []  # An arraylist for all the particles

    def addParticle(self, x, y):
        self.particles.append(Particle(x, y))
        
    def display(self):
        for p in self.particles:
            p.display()
            
    def intersection(self):
        for p in self.particles:
            p.intersects(self.particles)
        
    def update(self):
        for i, p in enumerate(self.particles):
            p.update()
            if p.isDead(): self.particles.pop(i)