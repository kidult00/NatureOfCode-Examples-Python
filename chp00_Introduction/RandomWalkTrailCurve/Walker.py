# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!
from java.util import ArrayList

class Walker(object):
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.history = ArrayList()
    
    def display(self):
        stroke(255,0,0)
        ellipse(self.position.x, self.position.y, 16, 16)
        
        beginShape()
        stroke(0)
        for v in self.history:
            curveVertex(v.x, v.y)
        endShape()
    
    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        self.position.x += random(-10,10)
        self.position.y += random(-10,10)
        
        # Stay on the screen
        self.position.x = constrain(self.position.x, 0, width-10)
        self.position.y = constrain(self.position.y, 0, height-10)
        
        self.history.add(self.position.get())
        