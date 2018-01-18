# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Mover(object):
    def __init__(self):
        # The Mover tracks position, velocity, and acceleration
        # Start in the center
        self.position = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
    
        # The Mover's maximum speed
        self.topspeed = 5
        
    def update(self):
        # Compute a vector that points from position to mouse
        mouse = PVector(mouseX, mouseY)
        self.acceleration = PVector.sub(mouse, self.position)
        # Set magnitude of acceleration
        self.acceleration.setMag(0.2)
        
        # Velocity changes according to acceleration
        self.velocity.add(self.acceleration)
        # Limit the velocity by topspeed
        self.velocity.limit(self.topspeed)
        # position changes by velocity
        self.position.add(self.velocity)
        
        
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 48, 48)