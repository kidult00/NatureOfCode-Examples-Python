# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleSystem(object):

    def __init__(self, imgs):
        self.particles = []  
        self.textures = imgs

    def addParticle(self, x, y):
        r = int(random(len(self.textures)))
        self.particles.append(Particle(x, y, self.textures[r]))
        
    def applyForce(self, f):
        for p in self.particles:
            p.applyForce(f)
                
    def display(self):
        for p in self.particles:
            p.display()
                
    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.isDead(): self.particles.pop(i)
            
    def dead(self):
        return self.particles.isEmpty()