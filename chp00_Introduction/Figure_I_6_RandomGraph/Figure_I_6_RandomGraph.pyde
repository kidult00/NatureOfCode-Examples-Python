# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(400, 200)
    smooth()

def draw():
    background(255)
    noFill()
    stroke(0)
    strokeWeight(2)
    beginShape()
    for i in range(width):
        y = random(height)
        vertex(i, y)
    endShape()
    noLoop()