# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(200, 200)
    background(0)
    noStroke()
    global xoff, xstep
    xoff = 0.0
    xstep = 0.01

def draw():
    # Create an alpha blended background
    fill(0, 10)
    rect(0, 0, width, height) 
    global xoff, xstep
    
    # n = random(0, width)  # Try this line instead of noise
    
    # Get a noise value based on xoff and scale it according to the window's width
    n = noise(xoff) * width
    
    # With each cycle, increment xoff
    xoff += xstep
    
    # Draw the ellipse at the value produced by perlin noise
    fill(200)
    ellipse(n, height/2, 16, 16)