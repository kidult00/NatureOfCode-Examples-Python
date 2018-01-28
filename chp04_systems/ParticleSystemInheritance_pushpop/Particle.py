# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):
    """
    Simple Particle System
    """
    def __init__(self, l):
        self.position = l.get()
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.acceleration = PVector(0, 0.05)
        self.lifespan = 255.0
        
    def run(self):
        self.update()
        self.push()
        self.display()
        self.pop()

    # Method to update position
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.lifespan -= 2.0
    
    def push(self): 
        pushMatrix()
        
    def pop(self):
        popMatrix()
    
    # Method to display
    def display(self):
        stroke(0, self.lifespan)
        fill(0, self.lifespan)
        translate(self.position.x, self.position.y)
        ellipse(0, 0, 8, 8)
        
    # Is the particle still useful?
    def isDead(self):
        if self.lifespan < 0.0 : return True
        else: return False