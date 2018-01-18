# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Spring(object):
    """
    Class to describe an anchor point that can connect to "Bob" objects via a spring
    Thank you: http://www.myphysicslab.com/spring2d.html
    """
    def __init__(self, x, y, l):
        self.anchor = PVector(x, y) # position
        self.len = l
        self.k = 0.2 # spring constant
        
    # Calculate spring force
    def connect(self, b):
        force = PVector.sub(b.position, self.anchor) # Vector pointing from anchor to bob position
        d = force.mag()  # What is distance
        stretch = d - self.len  # Stretch is difference between current distance and rest length
        
        # Calculate force according to Hooke's Law : F = k * stretch
        force.normalize()
        force.mult(- self.k * stretch)
        b.applyForce(force)
        
    # Constrain the distance between bob and anchor between min and max
    def constrainLength(self, b, minlen, maxlen):
        dir = PVector.sub(b.position, self.anchor)
        d = dir.mag()
        # Is it too short?
        if d < minlen :
            dir.normalize()
            dir.mult(minlen)
            # Reset position and stop from moving (not realistic physics)
            b.position = PVector.add(self.anchor, dir)
            b.velocity.mult(0)
        # Is it too long?
        elif d > maxlen :
            dir.normalize()
            dir.mult(maxlen)
            # Reset position and stop from moving (not realistic physics)
            b.position = PVector.add(self.anchor, dir)
            b.velocity.mult(0)
            
    def display(self):
        stroke(0)
        fill(175)
        strokeWeight(2)
        rectMode(CENTER)
        rect(self.anchor.x, self.anchor.y, 10, 10)
        
    def displayLine(self, b):
        stroke(0)
        strokeWeight(2)
        line(b.position.x, b.position.y, self.anchor.x, self.anchor.y)