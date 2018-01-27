# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Repeller(object):
    """A very basic Repeller class"""
    def __init__(self, x, y):
        self.G = 100.0  # force should be float!
        self.position = PVector(x, y)
        self.r = 10
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(175)
        ellipse(self.position.x, self.position.y, 48, 48)
        
    # Calculate a force to push particle away from repeller
    def repel(self, p):
        dir = PVector.sub(self.position, p.position)  # Calculate direction of force
        d = dir.mag()              # Distance between objects
        dir.normalize()             # Normalize vector (distance doesn't matter here, we just want this vector for direction)
        d = constrain(d, 5, 100)   # Keep distance within a reasonable range
        force = - self.G / (d * d) # Repelling force is inversely proportional to distance
        dir.mult(force)
        return dir