# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Force = Mass * Acceleration

class Mover(object):
    
    def __init__(self):
        self.position = PVector(400, 50)
        self.velocity = PVector(1, 0)
        self.acceleration = PVector(0, 0)
        self.mass = 1 # Mass is tied to size
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass) # bigger ones move slower
        self.acceleration.add(f) # Accumulate all forces in acceleration
        
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
        fill(127)
        ellipse(self.position.x, self.position.y, 16, 16)
        
    # Bounce off bottom of window
    def checkEdges(self):
        if self.position.x > width : 
            self.position.x = width
            self.velocity.x *= -0.5
        elif self.position.x < 0 : 
            self.position.x = 0
            self.velocity.x *= -0.5
        
        if self.position.y > height :
            self.velocity.y *= -0.5
            self.position.y = height
        elif self.position.y < 0:
            self.velocity.y *= -0.5
            self.position.y = 0