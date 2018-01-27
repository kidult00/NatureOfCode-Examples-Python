# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)
from Particle import Particle

# Simple Particle System

# A class to describe a group of Particles
# An ArrayList is used to manage the list of Particles 

class ParticleSystem(object):

    def __init__(self, num, v):
        self.particles = []  # An arraylist for all the particles
        self.origin = v      # An origin point for where particles are birthed
        for i in range(num):
            self.particles.append(Particle(self.origin)) # Add "num" amount of particles to the arraylist

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

    