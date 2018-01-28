# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):

    """Simple Particle System"""

    def __init__(self, x, y, r):
        self.position = PVector(x, y)
        self.velocity = PVector.random2D()
        self.velocity.mult(0.5)
        self.acceleration = PVector(0, 0.02)
        self.lifespan = 255.0
        self.r = r

    def run(self):
        self.update()
        self.display()

    # Method to update position
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.lifespan -= 2.0

    # Method to display
    def display(self):
        stroke(0, self.lifespan)
        fill(0)
        rectMode(CENTER)
        rect(self.position.x, self.position.y, self.r, self.r)

    # Is the particle still useful?
    def isDead(self):
        return self.lifespan < 0.0