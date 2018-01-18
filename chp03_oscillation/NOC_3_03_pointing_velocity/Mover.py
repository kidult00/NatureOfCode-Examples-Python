# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Force = Mass * Acceleration, Friction = Coefficient * NormalForce

class Mover(object):
    
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.topspeed = 4.0
        self.xoff = 1000.0
        self.yoff = 0.0
        self.r = 16.0
        
    def update(self):
        mouse = PVector(mouseX, mouseY)
        dir = PVector.sub(mouse, self.position)
        dir.normalize()
        dir.mult(0.5)
        self.acceleration = dir
        
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)
        
        
    def display(self):
        theta = self.velocity.heading()
        
        stroke(0)
        strokeWeight(2)
        fill(0, 127)
        
        pushMatrix()
        rectMode(CENTER)
        translate(self.position.x, self.position.y)
        rotate(theta)
        rect(0, 0, 30, 10)
        popMatrix()
        
    def checkEdges(self):
        if self.position.x > width : self.position.x = 0
        elif self.position.x < 0 : self.position.x = width
            
        if self.position.y > height : self.position.y = 0
        elif self.position.y < 0 : self.position.y = height