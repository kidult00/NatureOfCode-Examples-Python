# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!
from java.util import ArrayList
class Walker(object):
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.velocity = PVector()
        self.history = ArrayList()
        self.noff = PVector(random(1000), random(1000))
        
    def display(self):
        stroke(0)
        fill(175)
        rectMode(CENTER)
        rect(self.position.x, self.position.y, 16, 16)
        
        beginShape()
        stroke(0)
        noFill()
        for v in self.history:
            vertex(v.x, v.y)
        endShape()
    
    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        
        self.velocity.x = map(noise(self.noff.x), 0, 1, -1, 1)
        self.velocity.y = map(noise(self.noff.y), 0, 1, -1, 1)
        self.velocity.mult(5) # Multiply a vector by a scalar
    
        self.noff.add(0.01, 0.01, 0)
        
        self.position.add(self.velocity)
        
        self.history.add(self.position.get())
        if self.history.size() > 1000 : 
            self.history.remove(0)
        
        # Stay on the screen
        self.position.x = constrain(self.position.x, 0, width-1)
        self.position.y = constrain(self.position.y, 0, height-1)