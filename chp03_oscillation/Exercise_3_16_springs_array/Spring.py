# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Spring(object):
    """
    Class to describe an anchor point that can connect to "Bob" objects via a spring
    Thank you: http://www.myphysicslab.com/spring2d.html
    """
    def __init__(self, a_, b_, l):
        self.len = l
        self.k = 0.2 # spring constant
        self.a = a_
        self.b = b_
        
    # Calculate spring force
    def update(self):
        force = PVector.sub(self.a.position, self.b.position) # Vector pointing from anchor to bob position
        d = force.mag()  # What is distance
        stretch = d - self.len  # Stretch is difference between current distance and rest length
        
        # Calculate force according to Hooke's Law : F = k * stretch
        force.normalize()
        force.mult(- self.k * stretch)
        self.a.applyForce(force)
        force.mult(-1)
        self.b.applyForce(force)
        
            
    def display(self):
        stroke(0)
        strokeWeight(2)
        line(self.a.position.x, self.a.position.y, self.b.position.x, self.b.position.y)