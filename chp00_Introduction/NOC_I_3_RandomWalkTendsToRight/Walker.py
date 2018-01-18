# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2    
    
    def render(self):
        stroke(0)
        point(self.x, self.y)
    
    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        
        r = random(1) 
        
        # A 40% of moving to the right!
        if r < 0.4 :
            self.x += 1
        elif r < 0.6 :
            self.x -= 1
        elif r < 0.8 :
            self.y += 1
        else:
            self.y -= 1
        
        # Stay on the screen
        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)