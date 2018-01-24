# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Particle import Particle

class Wave(object):
    def __init__(self, o, w_, a, p):
        self.xspacing = 8     # How far apart should each horizontal position be spaced
        self.w = w_           # Width of entire wave
        self.origin = o.get() # Where does the wave's first point start
        self.theta = 0.0      # Start angle at 0
        self.amplitude = a
        self.period = p
        self.dx = TWO_PI / self.period * self.xspacing
        # self.yvalues = [None] * (self.w / self.xspacing)
        self.particles = [None] * (self.w / self.xspacing)
        
        for i,particle in enumerate(self.particles):
            self.particles[i] = Particle()
        
    def calculate(self):
        # Increment theta (try different values for 'angular velocity' here
        self.theta += 0.02
        
        # For every x value, calculate a y value with sine function
        x = self.theta
        for i in range(len(self.particles)):
            self.particles[i].setposition(self.origin.x+i*self.xspacing, 
                                          self.origin.y+sin(x)*self.amplitude)
            x += self.dx
    
    def manipulate(self):
        # Loop through the array of self.particles and check stuff regarding 
        # the mouse
        pass
                
    def display(self):
        # A simple way to draw the wave with an ellipse at each position
        for each in self.particles:
            each.display()