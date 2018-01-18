# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(800, 200)
    smooth()
    global x, y, xspeed, yspeed
    x = 100
    y = 100
    xspeed = 2.5
    yspeed = 2
    
def draw():
    background(255)
    global x, y, xspeed, yspeed
    # Add the current speed to the position
    x += xspeed
    y += yspeed
    
    if x > width or x < 0 :
        xspeed *= -1
    if y > height or y < 0 :
        yspeed *= -1
    
    # Display circle at x position
    stroke(0)
    strokeWeight(2)
    fill(127)
    ellipse(x, y, 48, 48)