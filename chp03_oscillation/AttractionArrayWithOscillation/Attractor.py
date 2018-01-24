# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Attractor(object):
    """
    Attraction
    A class for a draggable attractive body in our world
    """
    def __init__(self, l_, m_, g_):
        self.mass = m_        # Mass, tied to size
        self.G = g_           # Gravitational Constant
        self.pos = l_.get()   # position
        self.dragging = False # Is the object being dragged?
        self.rollover_s = False # Is the mouse over the ellipse?
        self.drag_v = PVector(0.0, 0.0)  # holds the offset for when object is clicked on
        
    def go(self):
        self.render()
        self.drag()
        
        
    def attract(self, c):
        dir = PVector.sub(self.pos, c.pos)  # Calculate direction of force
        d = dir.mag()                       # Distance between objects
        d = constrain(d, 5.0, 25.0)         # Limiting the distance to eliminate "extreme" results for very close or very far objects
        dir.normalize()                     # Normalize vector (distance doesn't matter here, we just want this vector for direction)
        force = (self.G * self.mass * c.mass) / (d * d)  # Calculate gravitional force magnitude
        dir.mult(force)                     # Get force vector --> magnitude * direction
        return dir
    
    # Method to display
    def render(self):
        ellipseMode(CENTER)
        stroke(0, 100)
        if self.dragging: fill(50)
        elif self.rollover_s: fill(100)
        else : fill(175, 50)
        ellipse(self.pos.x, self.pos.y, self.mass*2, self.mass*2)
        
    # The methods below are for mouse interaction
    def clicked(self, mx, my):
        d = dist(mx, my, self.pos.x, self.pos.y)
        if d < self.mass :
            self.dragging = True
            self.drag_v.x = self.pos.x - mx
            self.drag_v.y = self.pos.y - my
            
    def rollover(self, mx, my):
        d = dist(mx, my, self.pos.x, self.pos.y)
        if d < self.mass : 
            self.rollover_s = True
        else : 
            self.rollover_s = False
        
    def stopDragging(self):
        self.dragging = False
        
    def drag(self):
        if self.dragging :
            self.pos.x = mouseX + self.drag_v.x
            self.pos.y = mouseY + self.drag_v.y