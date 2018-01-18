# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!
from java.util import ArrayList

class Walker(object):
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.history = ArrayList()
    
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
        vel = PVector(int(random(-2,2)), int(random(-2,2)))
        self.position.add(vel)
        print(self.position)
        
        # Stay on the screen
        self.position.x = constrain(self.position.x, 0, width-1)
        self.position.y = constrain(self.position.y, 0, height-1)
        
        self.history.add(self.position.get())
        # print(self.history)
        if self.history.size() > 1000:
            self.history.remove(0)