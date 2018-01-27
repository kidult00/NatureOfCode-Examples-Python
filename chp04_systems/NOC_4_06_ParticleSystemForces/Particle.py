# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):
    """
    Simple Particle System
    """
    def __init__(self, l):
        self.position = l.get()
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.acceleration = PVector(0, 0)
        self.lifespan = 255.0
        self.mass = 1
        
    def run(self):
        self.update()
        self.display()

    def applyForce(self, force):
        f = force.get()
        f.div(self.mass)
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
        ellipse(self.position.x, self.position.y, 12, 12)
        
    # Is the particle still useful?
    def isDead(self):
        if self.lifespan < 0.0 : return True
        else: return False