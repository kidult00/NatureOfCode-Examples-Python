# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class ParticleChild(Particle):

    # def __init__(self, l):
    #     super(ParticleChild, self).__init__(l)

    # Override the display method
    def display(self):
        super(ParticleChild, self).display()
        theta = map(self.position.x, 0, width, 0, TWO_PI * 2)
        rotate(theta)
        stroke(0)
        line(0, 0, 50, 0)
