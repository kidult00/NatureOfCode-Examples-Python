# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(640, 360)


def draw():
    background(255)
    period = 120
    amplitude = 300
    # Calculating horizontal position according to formula for simple harmonic motion
    x = amplitude * sin(TWO_PI * frameCount / period)

    fill(127)
    stroke(0)
    strokeWeight(2)
    translate(width/2, height/2)
    line(0, 0, x, 0)
    ellipse(x, 0, 48, 48)
