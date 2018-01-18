# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.tx = 0
        self.ty = 10000
        self.x = map(noise(self.tx), 0, 1, 0, width)
        self.y = map(noise(self.ty), 0, 1, 0, height)
    
    def render(self):
        stroke(255)
        line(prevX, prevY, self.x, self.y)
    
    # Randomly move according to floating point values
    def step(self):
        global prevX, prevY
        prevX = self.x
        prevY = self.y
        
        self.x = map(noise(self.tx), 0, 1, 0, width)
        self.y = map(noise(self.ty), 0, 1, 0, height)
    
        self.tx += 0.01
        self.ty += 0.01