# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleSystem(object):

    def __init__(self):
        self.particles = []  # An arraylist for all the particles
        
        
    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)

    def addParticle(self, x, y, force):
        self.particles.append(Particle(PVector(x, y), force))
        
    # A method to test if the particle system still has particles
    def dead(self):
        if self.particles.isEmpty(): return True
        else: return False

    