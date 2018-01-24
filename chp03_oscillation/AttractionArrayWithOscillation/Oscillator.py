# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Oscillator(object):
    """
    Attraction Array with Oscillating objects around each thing
    """
    def __init__(self, r):
        # Because we are going to oscillate along the x and y axis we can use PVector for two angles, amplitudes, etc.!
        self.theta = 0
        self.amplitude = r
        
    # Update theta and offset
    def update(self, thetaVel):
        self.theta += thetaVel
        
    # Display based on a position
    def display(self, pos):
        x = map(cos(self.theta), -1, 1, 0, self.amplitude)
        
        stroke(0)
        fill(50)
        line(0, 0, x, 0)
        ellipse(x, 0, 8, 8)