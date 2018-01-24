# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Bob(object):
    """
    Bob class, just like our regular Mover (position, velocity, acceleration, mass)
    """
    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector()
        self.acceleration = PVector()
        self.mass = 12
        self.damping = 0.95 # Arbitrary damping to simulate friction / drag
        self.dragOffset = PVector()
        self.dragging = False
        
    # Standard Euler integration
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.mult(self.damping)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        
    # Newton's law: F = M * A
    def applyForce(self, force):
        f = force.get()
        f.div(self.mass)
        self.acceleration.add(f)
        
    # Draw the bob
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(175)
        if self.dragging : fill(50)
        ellipse(self.position.x, self.position.y, self.mass * 2, self.mass * 2)
        
        
    # The methods below are for mouse interaction

    # This checks to see if we clicked on the mover
    def clicked(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass :
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my
            
    def stopDragging(self):
        self.dragging = False
        
    def drag(self, mx, my):
        if self.dragging :
            self.position.x = mx + self.dragOffset.x
            self.position.y = my + self.dragOffset.y