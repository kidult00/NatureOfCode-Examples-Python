# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Force = Mass * Acceleration, Friction = Coefficient * NormalForce

class Mover(object):
    
    def __init__(self, m, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.mass = m # Mass is tied to size
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass) # bigger ones move slower
        # Accumulate all forces in acceleration 
        self.acceleration.add(f)
        
    def update(self):
        # Velocity changes according to acceleration
        self.velocity.add(self.acceleration)
        # position changes by velocity
        self.position.add(self.velocity)
        # prevent cumulative acceleration
        self.acceleration.mult(0) 
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127, 200)
        ellipse(self.position.x, self.position.y, self.mass * 16, self.mass *16)
        
    # Bounce off bottom of window
    def checkEdges(self):
        if self.position.y > height :
            self.velocity.y *= -0.9
            self.position.y = height