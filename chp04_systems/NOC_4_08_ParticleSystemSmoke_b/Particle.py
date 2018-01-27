# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Particle(object):
    """
    Simple Particle System
    """
    def __init__(self, l, img_):
        self.position = l.get()
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.acceleration = PVector(0, 0)
        self.lifespan = 100.0
        self.vx = randomGaussian() * 0.3
        self.vy = randomGaussian() * 0.3 - 1.0
        self.img = img_
        
    def run(self):
        self.update()
        self.display()

    def applyForce(self, force):
        # f = force.get()
        # f.div(self.mass)
        self.acceleration.add(force)
    
    # Method to update position
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # clear Acceleration
        self.lifespan -= 2.5
    
    # Method to display
    def display(self):
        # imageMode(CENTER)
        # tint(255, self.lifespan)
        # image(self.img, self.position.x, self.position.y)
        # stroke(0, self.lifespan)
        # strokeWeight(2)
        fill(255, self.lifespan)
        noStroke()
        ellipse(self.position.x, self.position.y, self.img.width, self.img.height)
        
    # Is the particle still useful?
    def isDead(self):
        if self.lifespan < 0.0 : return True
        else: return False