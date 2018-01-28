# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):

    """Simple Particle System"""

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector.random2D()
        self.acceleration = PVector()
        self.lifespan = 255.0
        self.r = 6

    def run(self):
        self.update()
        self.display()

    def intersects(self, particles):
        self.highlight = False
        for p in particles:
            if p != self:
                dir = PVector.sub(p.position, self.position)
                if dir.mag() < self.r*2:
                    dir.setMag(0.5)
                    self.applyForce(dir)

    def applyForce(self, f):
        self.acceleration.add(f)

    # Method to update position
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.lifespan -= 0.5

    # Method to display
    def display(self):
        stroke(0, self.lifespan)
        strokeWeight(2)
        fill(127, self.lifespan)
        ellipse(self.position.x, self.position.y, self.r*2, self.r*2)

    # Is the particle still useful?
    def isDead(self):
        return self.lifespan < 0.0