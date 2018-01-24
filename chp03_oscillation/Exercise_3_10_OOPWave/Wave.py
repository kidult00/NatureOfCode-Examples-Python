# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Wave(object):
    def __init__(self, o, w_, a, p):
        self.xspacing = 8     # How far apart should each horizontal position be spaced
        self.w = w_           # Width of entire wave
        self.origin = o.get() # Where does the wave's first point start
        self.theta = 0.0      # Start angle at 0
        self.amplitude = a
        self.period = p
        self.dx = TWO_PI / self.period * self.xspacing
        self.yvalues = [None] * (self.w / self.xspacing)
        
    def calculate(self):
        # Increment theta (try different values for 'angular velocity' here
        self.theta += 0.02
        
        # For every x value, calculate a y value with sine function
        x = self.theta
        for i in range(len(self.yvalues)):
            self.yvalues[i] = sin(x) * self.amplitude
            x += self.dx
        
    def display(self):
        # A simple way to draw the wave with an ellipse at each position
        stroke(0)
        fill(0, 50)
        ellipseMode(CENTER)
        for x in range(len(self.yvalues)):
            ellipse(self.origin.x + x * self.xspacing, self.origin.y + self.yvalues[x], 48, 48)