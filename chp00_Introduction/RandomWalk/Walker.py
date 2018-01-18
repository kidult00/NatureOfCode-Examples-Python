# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2    
    
    def render(self):
        stroke(0)
        fill(175)
        rectMode(CENTER)
        rect(self.x, self.y, 40, 40)
    
    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        vx = random(-2, 2)
        vy = random(-2, 2)
        self.x += vx
        self.y += vy
        
        # Stay on the screen
        x = constrain(self.x, 0, width-1)
        
        y = constrain(self.y, 0, height-1)