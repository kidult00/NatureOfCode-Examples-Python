# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.pos = PVector(width/2, height/2)
    
    def render(self):
        stroke(0)
        fill(175)
        rectMode(CENTER)
        rect(self.pos.x, self.pos.y, 40, 40)
    
    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        vel = PVector(random(-2,2), random(-2,2))
        self.pos.add(vel)
        
        # Stay on the screen
        self.pos.x = constrain(self.pos.x, 0, width-1)
        
        self.pos.y = constrain(self.pos.y, 0, height-1)