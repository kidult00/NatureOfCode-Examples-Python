# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Force = Mass * Acceleration

class Mover(object):
    
    def __init__(self, m, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
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
        strokeWeight(2)
        fill(0, 100)
        ellipse(self.position.x, self.position.y, self.mass * 24, self.mass * 24)
        
    def attract(self, mover):
        force = PVector.sub(self.position, mover.position)
        distance = force.mag()
        distance = constrain(distance, 5.0, 25.0)
        force.normalize()
        
        strength = (0.4 * self.mass * mover.mass) / (distance * distance)
        force.mult(strength)
        return force
        