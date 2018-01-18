# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2
    
    def render(self):
        stroke(255)
        line(prevX, prevY, self.x, self.y)
    
    def montecarlo(self):
        while True:
            r1 = random(1)
            probability = pow(1.0 - r1, 8)
            r2 = random(1)
            if r2 < probability :
                return r1
    
    # Randomly move according to floating point values
    def step(self):
        global prevX, prevY
        prevX = self.x
        prevY = self.y
        
        stepx = random(-1, 1)
        stepy = random(-1, 1)
        
        stepsize = self.montecarlo()*50
        stepx *= stepsize 
        stepy *= stepsize
        
        self.x += stepx
        self.y += stepy
        
        # Stay on the screen
        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)