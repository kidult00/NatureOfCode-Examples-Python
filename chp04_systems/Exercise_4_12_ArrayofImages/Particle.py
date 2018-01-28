# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):

    """Simple Particle System"""

    def __init__(self, x, y, img):
        self.position = PVector(x, y)
        self.velocity = PVector.random2D()
        self.acceleration = PVector(0, 0)
        self.lifespan = 255
        self.img = img

    def run(self):
        self.update()
        self.display()

    def applyForce(self, f):
        self.acceleration.add(f)

    # Method to update position
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.lifespan -= 2

    # Method to display
    def display(self):
        imageMode(CENTER)
        tint(self.lifespan)
        image(self.img, self.position.x, self.position.y, 32, 32)

    # Is the particle still useful?
    def isDead(self):
        return self.lifespan < 0.0