# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(640, 360)
    background(255)


def draw():
    
    # Get a gaussian random number w/ mean of 0 and standard deviation of 1.0
    xloc = randomGaussian()
    print(xloc)
    
    sd = 60.0      # Define a standard deviation
    mean = width/2 # Define a mean value (middle of the screen along the x-axis)
    xloc = (xloc * sd) + mean # Scale the gaussian random number by standard deviation and mean
    
    fill(0,10)
    noStroke()
    ellipse(xloc, height/2, 16, 16)