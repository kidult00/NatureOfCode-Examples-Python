# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# A class for a draggable attractive body in our world
# Attraction = G * M1 * M2 / Distance^2

class Attractor(object):
    def __init__(self):
        self.mass = 20.0 # Mass, tied to size
        self.g = 0.4     # Gravitational Constant
        self.position = PVector(0, 0)
        
    def attract(self, m):
        force = PVector.sub(self.position, m.position)  # Calculate direction of force
        d = force.mag()               # Distance between objects
        d = constrain(d, 5.0, 25.0)   # Limiting the distance to eliminate "extreme" results for very close or very far objects
        force.normalize()             # Normalize vector (distance doesn't matter here, we just want this vector for direction)
        strength = (self.g * self.mass * m.mass) / (d * d) # Calculate gravitional force magnitude
        force.mult(strength) # Get force vector --> magnitude * direction
        return force
    
    # Method to display
    def display(self):
        stroke(0)
        noFill()
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        sphere(self.mass * 2)
        popMatrix()
        