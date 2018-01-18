# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# PolarToCartesian
# Convert a polar coordinate (r,theta) to cartesian (x,y):  
# x = r * cos(theta)
# y = r * sin(theta)

def setup():
    size(800, 200)
    background(255)
    global r, theta
    r = height * 0.45
    theta = 0.0    

def draw():
    noStroke()
    fill(255, 5)
    rect(0, 0, width, height)
    
    # Translate the origin point to the center of the screen
    translate(width/2, height/2)
    
    global r, theta
    # Convert polar to cartesian
    x = r * cos(theta);
    y = r * sin(theta)

    # Draw the ellipse at the cartesian coordinate
    ellipseMode(CENTER)
    fill(127)
    stroke(0)
    strokeWeight(2)
    line(0, 0, x, y)
    ellipse(x, y, 48, 48)
    
    # Increase the angle over time
    theta += 0.02