# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.noff = PVector(random(1000), random(1000))
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 48, 48)
    
    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        
        self.position.x = map(noise(self.noff.x), 0, 1, 0, width)
        self.position.y = map(noise(self.noff.y), 0, 1, 0, height)
    
        self.noff.x += 0.01
        self.noff.y += 0.01