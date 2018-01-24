# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Mover(object):
    def __init__(self):
        self.position = PVector(400, 50)
        self.velocity = PVector(1, 0)
        self.acceleration = PVector(0, 0)
        self.mass = 1 


    def applyForce(self, force):
        f = PVector.div(force, self.mass) 
        self.acceleration.add(f) 
        
    def update(self):
        self.velocity.add(self.acceleration) # Velocity changes according to acceleration
        self.position.add(self.velocity) # position changes by velocity
        self.acceleration.mult(0) # prevent cumulative acceleration 
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        
        pushMatrix()
        translate(self.position.x, self.position.y)
        heading = self.velocity.heading()
        rotate(heading)
        ellipse(0, 0, 16, 16)
        rectMode(CENTER)
        # "20" should be a variable that is oscillating with sine function
        rect(20, 0, 10, 10)
        popMatrix()

    def checkEdges(self):
        if self.position.x > width : self.position.x = 0
        elif self.position.x < 0 : self.position.x = width
        
        if self.position.y > height : 
            self.position.y *= -1
            self.position.y = height
        