# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(750, 200)
    background(255)
    smooth()
    global r, theta
    r = 0
    theta = 0
    

def draw():
    global r, theta
    # Polar to Cartesian conversion
    x = r * cos(theta)
    y = r * sin(theta)
    
    # Draw an ellipse at x, y
    noStroke()
    fill(0)
    ellipse(x + width/2, y + height/2, 16, 16)
    
    # Increment the angle
    theta += 0.01
    
    # Increment the redius
    r += 0.05