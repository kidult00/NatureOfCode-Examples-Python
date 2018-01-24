# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):
    def __init__(self):
        self.position = PVector()
        
    def setposition(self, x, y):
        self.position.x = x
        self.position.y = y
        
    def display(self):
        fill(random(255))
        ellipse(self.position.x, self.position.y, 16, 16)