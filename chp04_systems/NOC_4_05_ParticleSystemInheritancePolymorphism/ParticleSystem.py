# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)
from Particle import Particle
from Confetti import Confetti

# Simple Particle System

# A class to describe a group of Particles
# An ArrayList is used to manage the list of Particles 

class ParticleSystem(object):

    def __init__(self, position):
        self.particles = []     # An arraylist for all the particles
        self.origin = position.get()  # An origin point for where particles are birthed
        
    def addParticle(self):
        r = random(1)
        if r < 0.5: self.particles.append(Particle(self.origin))
        else: self.particles.append(Confetti(self.origin))
        
    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)