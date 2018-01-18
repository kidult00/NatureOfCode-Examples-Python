# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Force = Mass * Acceleration

class Mover(object):
    
    def __init__(self, m, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.mass = m
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass) # bigger ones move slower 
        self.acceleration.add(f)
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # prevent cumulative acceleration
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(0, 127)
        ellipse(self.position.x, self.position.y, self.mass * 16, self.mass *16)
        
    def checkEdges(self):
        if self.position.x > width :
            self.position.x = width
            self.velocity.x *= -1
        elif self.position.x < 0 :
            self.velocity.x *= -1
            self.position.x = 0
            
        if self.position.y > height :
            self.velocity.y *= -1
            self.position.y = height