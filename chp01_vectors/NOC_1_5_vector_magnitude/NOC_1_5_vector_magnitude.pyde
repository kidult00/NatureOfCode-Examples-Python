# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Example 1-4: Vector multiplication
def setup():
    size(640, 360)
    
def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    center = PVector(width/2, height/2)
    mouse.sub(center)
    
    # Multiplying a vector!  The vector is now half its original size (multiplied by 0.5).
    m = mouse.mag()
    fill(0)
    noStroke()
    rect(0, 0, m, 10)
    
    translate(width/2, height/2)
    strokeWeight(2)
    stroke(0)
    line(0, 0, mouse.x, mouse.y)