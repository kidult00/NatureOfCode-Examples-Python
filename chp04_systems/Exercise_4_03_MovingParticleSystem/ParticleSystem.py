# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleSystem(object):

    def __init__(self, position):
        self.particles = []  # An arraylist for all the particles
        self.origin = position.get()      # An origin point for where particles are birthed
        
    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)

    def addParticle(self):
        self.particles.append(Particle(self.origin))
        
    # A method to test if the particle system still has particles
    def dead(self):
        if self.particles.isEmpty(): return True
        else: return False

    