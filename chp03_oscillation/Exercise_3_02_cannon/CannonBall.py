# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class CannonBall(object):
    def __init__(self, x, y):
        # All of our regular motion stuff
        self.position = PVector(x, y)
        self.velocity = PVector()
        self.acceleration = PVector()
        self.r = 8 # Size
        self.topspeed = 10
    
    # Standard Euler integration
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        
    def applyForce(self, force):
        self.acceleration.add(force)
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        pushMatrix()
        translate(self.position.x, self.position.y)
        ellipse(0, 0, self.r*2, self.r*2)
        popMatrix()