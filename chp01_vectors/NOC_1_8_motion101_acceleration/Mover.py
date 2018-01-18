# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Mover(object):
    def __init__(self):
        self.position = PVector(random(width), random(height))
        self.velocity = PVector(random(-2, 2), random(-2, 2))
        self.acceleration = PVector(-0.001, 0.01)
        self.topspeed = 10
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)
        
    def checkEdges(self):
        if self.position.x > width : self.position.x = 0
        if self.position.x < 0 : self.position.x = width
        if self.position.y > height : self.position.y = 0
        if self.position.y < 0 : self.position.y = height
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 48, 48)