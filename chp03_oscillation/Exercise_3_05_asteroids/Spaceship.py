# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Spaceship(object):
    def __init__(self):
        # All of our regular motion stuff
        self.position = PVector(width/2, height/2)
        self.velocity = PVector()
        self.acceleration = PVector()
        self.damping = 0.995 # Arbitrary damping to slow down ship
        self.topspeed = 6
        self.heading = 0 # Variable for heading!
        self.r = 16  # Size
        self.thrusting = False # Are we thrusting (to color boosters)
    
    # Standard Euler integration
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.mult(self.damping)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        
    # Newton's law: F = M * A
    def applyForce(self, force):
        f = force.get()
        self.acceleration.add(f)

    # Turn changes angle
    def turn(self, a):
        self.heading += a

    # Turn changes angle
    def thrust(self):
        # Offset the angle since we drew the ship vertically
        angle = self.heading - PI/2
        # Polar to cartesian for force vector!
        force = PVector(cos(angle), sin(angle))
        force.mult(0.1)
        self.applyForce(force)
        # To draw booster
        self.thrusting = True
        
    def wrapEdges(self):
        buffer = self.r * 2
        if self.position.x > width + buffer  : self.position.x = - buffer
        elif self.position.x < - buffer: self.position.x = width + buffer
        
        if self.position.y > height + buffer  : self.position.y = - buffer
        elif self.position.y < - buffer: self.position.y = height + buffer
    
    # Draw the ship
    def display(self):
        stroke(0)
        strokeWeight(2)
        
        pushMatrix()
        translate(self.position.x, self.position.y + self.r)
        rotate(self.heading)
        fill(175)
    
        if self.thrusting : fill(255, 0, 0)
        
        # Booster rockets
        rect(-self.r/2, self.r, self.r/3, self.r/2)
        rect(self.r/2, self.r, self.r/3, self.r/2)
        fill(175)
        # A triangle
        beginShape()
        vertex(-self.r, self.r) # triangle left-down point
        vertex(0, -self.r)      # triangle top point
        vertex(self.r, self.r)  # triangle right-down point
        endShape(CLOSE)
        
        rectMode(CENTER)
        popMatrix()
        
        self.thrusting = False