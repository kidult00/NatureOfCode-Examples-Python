# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(200, 200)
    background(0)


def draw():
    # create an alpha blended background
    fill(0, 1)
    rect(0, 0, width, height)
    
    # get 3 gaussian random numbers w/ mean of 0 and standard deviation of 1.0
    r = randomGaussian()
    g = randomGaussian()
    b = randomGaussian()
    
    # define standard deviation and mean
    sd = 100.0
    mean = 100.0
    # scale by standard deviation and mean
    # also constrain to between (0,255) since we are dealing with color
    r = constrain(r * sd + mean, 0, 255)
    
    # repeat for g & b
    sd = 20 
    mean = 200
    g = constrain(r * sd + mean, 0, 255)
    sd = 50 
    mean = 0
    b = constrain(r * sd + mean, 0, 255)
    
    # get more gaussian numbers, this time for position
    xloc = randomGaussian()
    yloc = randomGaussian()
    sd = width/10
    mean = width/2
    xloc = xloc * sd + mean
    yloc = yloc * sd + mean
    # draw an ellipse with gaussian generated color and position
    noStroke()
    fill(r,g,b)
    ellipse(xloc,yloc,8,8)