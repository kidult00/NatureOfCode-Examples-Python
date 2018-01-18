# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Additive Wave
# Create a more complex wave by adding two waves together.

def setup():
    size(640, 360)
    colorMode(RGB, 255, 255, 255, 100)
    
    global xspacing, w, maxwaves, theta, yvalues, amplitude, dx
    xspacing = 8   # How far apart should each horizontal position be spaced
    w = width + 16 # Width of entire wave
    maxwaves = 5   # total # of waves to add together
    theta = 0.0
    amplitude = [None] * maxwaves  # Height of wave
    dx = [None] * maxwaves # Value for incrementing X, to be calculated as a function of period and xspacing
    
    for i in range(maxwaves):
        amplitude[i] = random(10, 30)
        period = random(100, 300) # How many pixels before the wave repeats
        dx[i] = (TWO_PI / period) * xspacing

    yvalues = [None] * (w/xspacing) # Using an array to store height values for the wave (not entirely necessary)


def draw():
    background(0)
    calcWave()
    renderWave()
    
def calcWave():
    global theta, yvalues, maxwaves, amplitude, dx
    # Increment theta (try different values for 'angular velocity' here
    theta += 0.02
    
    # Set all height values to zero
    yvalues = [0] * len(yvalues)
    
    # Accumulate wave height values
    for j in range(maxwaves):
        x = theta
        for i in range(len(yvalues)):
            # Every other wave is cosine instead of sine
            if (j % 2 == 0): yvalues[i] += sin(x) * amplitude[j]
            else: yvalues[i] += cos(x) * amplitude[j]
            x += dx[j]


def renderWave():
    # A simple way to draw the wave with an ellipse at each position
    noStroke()
    fill(255, 50)
    ellipseMode(CENTER)
    for x in range(len(yvalues)):
        ellipse(x * xspacing, height/2 + yvalues[x], 16, 16)
    
    