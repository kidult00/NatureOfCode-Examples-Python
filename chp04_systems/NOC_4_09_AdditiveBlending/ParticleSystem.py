# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleSystem(object):
    """
    A class to describe a group of Particles
    An ArrayList is used to manage the list of Particles 
    """
    def __init__(self, v, img):
        self.particles = []  # An arraylist for all the particles
        self.origin = v      # An origin point for where particles are birthed
        self.img = img
        
    def addParticle(self, p=None):
        if not p:
            self.particles.append(Particle(self.origin, self.img))
        else:
            self.particles.append(p)
        
    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)