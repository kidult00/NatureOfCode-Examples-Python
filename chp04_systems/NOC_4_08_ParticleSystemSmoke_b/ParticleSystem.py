# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleSystem(object):
    """
    Smoke Particle System
    A class to describe a group of Particles
    An ArrayList is used to manage the list of Particles 
    """
    def __init__(self, num, v, img_):
        self.particles = []  
        self.origin = v  
        self.img = img_
        for i in range(num):
            self.particles.append(Particle(self.orgin, self.img))   
        
    def applyForce(self, f):
        for each in self.particles: each.applyForce(f)

    def addParticle(self):
        self.particles.append(Particle(self.origin, self.img))
        
    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead():
                self.particles.pop(i)