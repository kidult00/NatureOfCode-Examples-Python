# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(400, 200)
    smooth()


def draw():
    background(255)
    e = 2.71828183           # "e", see http://mathforum.org/dr.math/faq/faq.e.html for more info
    heights = [None] * width # use an array to store all the "y" values
    m = 0.0                  # default mean of 0
    sd = map(mouseX, 0, width, 0.4, 2) # standard deviation based on mouseX
    
    for i in range(0, width):
        xcoord = float(map(i, 0, width, -3, 3))
        sq2pi = sqrt(2 * PI)         # square root of 2 * PI
        xmsq = -1 * (xcoord - m)**2  # -(x - mu)^2
        sdsq = sd**2                 # variance (standard deviation squared)
        heights[i] = (1 / (sd * sq2pi)) * (pow(e, (xmsq/sdsq))) # P(x) function
     
    # a little for loop that draws a line between each point on the graph       
    stroke(0)
    strokeWeight(2)
    noFill()
    beginShape()
    for i in range(0, width-1):
        x = i
        y = map(heights[i], 0, 1, height-2, 2)
        vertex(x, y)
    endShape()