# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):

    """Simple Particle System"""

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.acceleration = PVector(0, 0.05)
        self.lifespan = 255.0
        self.r = 6
        self.highlight = False

    def run(self):
        self.update()
        self.display()

    def intersects(self, particles):
        self.highlight = False
        for p in particles:
            if p != self:
                d = PVector.dist(p.position, self.position)
                if d < self.r:
                    self.highlight = True

    def applyForce(self, f):
        self.acceleration.add(f)

    # Method to update position
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.lifespan -= 2.0

    # Method to display
    def display(self):
        stroke(0, self.lifespan)
        strokeWeight(2)
        fill(127, self.lifespan)
        if self.highlight : fill(127, 0, 0)
        ellipse(self.position.x, self.position.y, self.r*2, self.r*2)

    # Is the particle still useful?
    def isDead(self):
        return self.lifespan < 0.0