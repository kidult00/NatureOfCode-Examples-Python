# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Force = Mass * Acceleration

class Mover(object):
    
    def __init__(self, m, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(random(-1,1), random(-1,1))
        self.acceleration = PVector(0, 0)
        self.mass = m # Mass is tied to size
        self.angle = 0.0
        self.aVelocity = 0.0
        self.aAcceleration = 0.0
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass) # bigger ones move slower
        self.acceleration.add(f) # Accumulate all forces in acceleration
        
    def update(self):
        
        self.velocity.add(self.acceleration) # Velocity changes according to acceleration
        self.position.add(self.velocity) # position changes by velocity
        
        self.aAcceleration = self.acceleration.x / 10.0
        self.aVelocity += self.aAcceleration
        self.aVelocity = constrain(self.aVelocity, -0.1, 0.1)
        self.angle += self.aVelocity
        
        self.acceleration.mult(0) # prevent cumulative acceleration 
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(175, 200)
        rectMode(CENTER)
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(self.angle)
        rect(0, 0, self.mass*16, self.mass*16)
        popMatrix()

        