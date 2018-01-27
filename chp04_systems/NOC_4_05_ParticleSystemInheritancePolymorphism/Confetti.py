# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class Confetti(Particle):

    def __init__(self, l):
        # Inherits update() from parent
        super(Confetti, self).__init__(l)

    # Override the display method
    def display(self):
        rectMode(CENTER)
        fill(127, self.lifespan)
        stroke(0, self.lifespan)
        strokeWeight(2)
        pushMatrix()
        translate(self.position.x, self.position.y)
        theta = map(self.position.x, 0, width, 0, TWO_PI * 2)
        rotate(theta)
        rect(0, 0, 12, 12)
        popMatrix()
