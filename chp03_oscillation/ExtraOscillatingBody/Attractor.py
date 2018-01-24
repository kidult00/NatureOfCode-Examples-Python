# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# A class for a draggable attractive body in our world
# Attraction = G * M1 * M2 / Distance^2

class Attractor(object):
    def __init__(self):
        self.mass = 20   # Mass, tied to size
        self.G = 1       # Gravitational Constant
        self.position = PVector(width/2, height/2)
        self.dragging = False                # Is the object being dragged?
        self.rollover = False                # Is the mouse over the ellipse?
        self.dragOffset = PVector(0.0, 0.0)  # holds the offset for when object is clicked on
        
    def attract(self, m):
        force = PVector.sub(self.position, m.position)  # Calculate direction of force
        d = force.mag()               # Distance between objects
        d = constrain(d, 5.0, 25.0)   # Limiting the distance to eliminate "extreme" results for very close or very far objects
        force.normalize()             # Normalize vector (distance doesn't matter here, we just want this vector for direction)
        strength = (self.G * self.mass * m.mass) / (d * d) # Calculate gravitional force magnitude
        force.mult(strength) # Get force vector --> magnitude * direction
        return force
    
    # Method to display
    def display(self):
        ellipseMode(CENTER)
        strokeWeight(4)
        stroke(0)
        if self.dragging : fill (50)
        elif self.rollover : fill(100)
        else: fill(175,200)
        ellipse(self.position.x, self.position.y, self.mass*2, self.mass*2)
        
    # The methods below are for mouse interaction
    def clicked(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass :
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my
            
    def hover(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass : self.rollover = True
        else : self.rollover = True
        
    def stopDragging(self):
        self.dragging = False
        
    def drag(self):
        if self.dragging :
            self.position.x = mouseX + self.dragOffset.x
            self.position.y = mouseY + self.dragOffset.y
        