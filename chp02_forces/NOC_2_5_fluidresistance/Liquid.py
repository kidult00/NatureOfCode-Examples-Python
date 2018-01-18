# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Liquid(object):
    def __init__(self, x_, y_, w_, h_, c_):
        # Liquid is a rectangle
        self.x = x_
        self.y = y_
        self.w = w_
        self.h = h_
        # Coefficient of drag
        self.c = c_
    
    # Is the Mover in the Liquid?    
    def contains(self, mover):
        l = mover.position
        return self.x < l.x < self.x + self.w and self.y < l.y < self.y + self.h
    
    # Calculate drag force
    def drag(self, mover):
        # Magnitude = coefficient * speed squared
        speed = mover.velocity.mag()
        dragMagnitude = self.c * speed * speed
        
        # Direction is inverse of velocity
        dragForce = mover.velocity.get()
        
        dragForce.normalize()
        dragForce.mult(-dragMagnitude)
        return dragForce
    
    def display(self):
        noStroke()
        fill(50)
        rect(self.x, self.y, self.w, self.h)
        
    