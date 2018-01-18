# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Mover(object):
    
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.mass = 1 # Mass is tied to size
        
    def shake(self):
        force = PVector.random2D()
        force.mult(0.7)
        self.applyForce(force)
    
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
        
        self.velocity.mult(0.95)
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 48, 48)
        
    def checkEdges(self):
        if self.position.x > width:
            self.position.x = width
            self.velocity.x *= -1
        elif self.position.x < 0 :
            self.position.x = 0
            self.velocity.x *= -1
            
        if self.position.y > height :
            self.position.y = height
            self.velocity.y *= -1