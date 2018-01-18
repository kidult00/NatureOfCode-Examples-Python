# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Force = Mass * Acceleration

class Mover(object):
    
    def __init__(self, m, x, y, z):
        self.position = PVector(x, y, z)
        self.velocity = PVector(1, 0)
        self.acceleration = PVector(0, 0)
        self.mass = m # Mass is tied to size
        
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
        fill(255)
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        sphere(self.mass * 8)
        popMatrix()
        
    def checkEdges(self):
        if self.x > width : self.position.x = 0
        if self.x < 0 : self.position.x = width
        if self.y > height : 
            self.position.y = height
            self.velocity.y *= -1