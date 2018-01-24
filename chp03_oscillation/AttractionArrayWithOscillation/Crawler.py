# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Oscillator import Oscillator

class Crawler(object):
    """
    Attraction
    A class to describe a thing in our world, has vectors for position, velocity, and acceleration
    Also includes scalar values for mass, maximum velocity, and elasticity
    """
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.vel = PVector(random(-1, 1), random(-1, 1))
        self.acc = PVector()
        self.mass = random(8, 16)
        self.osc = Oscillator(self.mass * 2)
        
    def applyForce(self, force):
        f = force.get()
        f.div(self.mass)
        self.acc.add(f)
        
    # Method to update position
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0) # Multiplying by 0 sets the all the components to 0
        self.osc.update(self.vel.mag() / 10)
        
    # Method to display
    def display(self):
        angle = self.vel.heading2D()
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(angle)
        ellipseMode(CENTER)
        stroke(0)
        fill(175, 100)
        ellipse(0, 0, self.mass*2, self.mass*2)
        
        self.osc.display(self.pos)
        popMatrix()