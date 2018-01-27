# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):
    """
    Simple Particle System
    """
    def __init__(self, l):
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.position = l.get()
        self.lifespan = 255.0
        
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
        strokeWeight(2)
        fill(127, self.lifespan)
        ellipse(self.position.x, self.position.y, 12, 12)
        
    # Is the particle still useful?
    def isDead(self):
        if self.lifespan < 0.0 : return True
        else: return False