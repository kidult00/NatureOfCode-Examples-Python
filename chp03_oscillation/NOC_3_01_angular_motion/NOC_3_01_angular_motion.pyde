# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(800, 200)
    smooth()
    global angle, aVelocity, aAcceleration
    angle = 0.0
    aVelocity = 0.0
    aAcceleration = 0.0001
    

def draw():
    background(255)
    fill(127)
    stroke(0)
    strokeWeight(2)
    global angle, aVelocity, aAcceleration
    
    translate(width/2, height/2)
    # rectMode(CENTER)
    rotate(angle)
    
    line(-60, 0, 60, 0)
    ellipse(60, 0, 16, 16)
    ellipse(-60, 0, 16, 16)
    
    angle += aVelocity
    aVelocity += aAcceleration