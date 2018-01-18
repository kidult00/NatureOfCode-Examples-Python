# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Pendulum(object):
    """
    A Simple Pendulum Class
    Includes functionality for user can click and drag the pendulum
    """
    
    # This constructor could be improved to allow a greater variety of pendulums
    def __init__(self, origin_, r_):
        self.position = PVector() # position of pendulum ball
        self.origin = origin_.get()  # position of arm origin
        self.r = r_            # Length of arm
        self.angle = PI / 4    # Pendulum arm angle
        self.aVelocity = 0.0     # Angle velocity
        self.aAcceleration = 0.0 # Angle acceleration
        self.ballr = 48          # Ball radius
        self.damping = 0.995     # Arbitary damping amount
        self.dragging = False

    def go(self):
        self.update()
        self.drag()   # for user interaction
        self.display()

    # Function to update position
    def update(self):
        # As long as we aren't dragging the pendulum, let it swing!
        if not self.dragging :
            gravity = 0.4                         # Arbitrary constant
            # Calculate acceleration (see: http://www.myphysicslab.com/pendulum1.html)
            self.aAcceleration = - gravity / self.r * sin(self.angle) 
            self.aVelocity += self.aAcceleration  # Increment velocity
            self.aVelocity *= self.damping        # Arbitrary damping
            self.angle += self.aVelocity          # Increment angle
        
        
    def display(self):
        # Polar to cartesian conversion
        self.position.set(self.r * sin(self.angle), self.r * cos(self.angle), 0)
        # Make sure the position is relative to the pendulum's origin
        self.position.add(self.origin)
        
        stroke(0)
        strokeWeight(2)
        # Draw the arm
        line(self.origin.x, self.origin.y, self.position.x, self.position.y)  
        
        ellipseMode(CENTER)
        fill(175)
        if self.dragging : fill(0)
        # Draw the ball
        ellipse(self.position.x, self.position.y, self.ballr, self.ballr)

    # The methods below are for mouse interaction
    
    # This checks to see if we clicked on the pendulum ball
    def clicked(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.ballr : 
            self.dragging = True
        
    # This tells us we are not longer clicking on the ball
    def stopDragging(self):
        self.aVelocity = 0 # No velocity once you let go
        self.dragging = False
        
    def drag(self):
        # If we are draging the ball, we calculate the angle between the 
        # pendulum origin and mouse position
        # we assign that angle to the pendulum
        if self.dragging :
            # Difference between 2 points
            diff = PVector.sub(self.origin, PVector(mouseX, mouseY))
            # Angle relative to vertical axis
            self.angle = atan2(- diff.y, diff.x) - radians(90) 