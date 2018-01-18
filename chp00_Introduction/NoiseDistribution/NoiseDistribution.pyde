# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Testing Distribution of Perlin Noise generated #'s vs. Randoms
def setup():
    size(300, 200)
    global vals, norms, xoff
    vals = [0.0] * width 
    norms = [0.0] * width
    xoff = 0.0

def draw():
    background(155)
    stroke(255)

    global vals, norms, xoff
    n = noise(xoff)
    index = int(n * width)
    vals[index] += 1
    xoff += 0.01
    normalization = False
    maxy = 0.0
    
    for x in range(len(vals)):
        line(x, height, x, height-norms[x])
        if vals[x] > height: normalization = True 
        if vals[x] > max: maxy = vals[x]
    
    for x in range(len(vals)):
        if normalization : 
            norms[x] = vals[x] / maxy * height
        else:
            norms[x] = vals[x]
     