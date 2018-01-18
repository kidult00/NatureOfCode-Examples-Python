# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(750, 150)
    smooth()
    global angle 
    angle = 0

def draw():
    background(255)
    fill(127)
    stroke(0)
    
    rectMode(CENTER)
    translate(width/2, height/2)
    
    global angle
    rotate(angle)
    line(-50, 0, 50, 0)
    strokeWeight(2)
    ellipse(50, 0, 16, 16)
    ellipse(-50, 0, 16, 16)
    
    angle += 0.05