# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleSystem(object):

    def __init__(self, x, y, r):
        self.particles = []
        self.rows = 20
        self.cols = 20
        self.intact = True
        for i in range(self.rows * self.cols):
            self.addParticle(x + (i % self.cols) * r, 
                             y + (i / self.rows) * r, r)

    def display(self):
        for p in self.particles:
            p.display()

    def addParticle(self, x, y, r):
        self.particles.append(Particle(x, y, r))

    def shatter(self):
        self.intact = False
        
    def update(self):
        if not self.intact:
            for p in self.particles:
                p.update()
