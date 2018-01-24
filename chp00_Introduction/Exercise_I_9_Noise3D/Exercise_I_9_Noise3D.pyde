# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(200, 200)

    global zoff, step, zstep
    # The noise function's 3rd argument, a global variable that increments once per cycle
    # We will increment zoff differently than xoff and yoff
    step = 0.01
    zoff = 0.0
    zstep = 0.02

def draw():
    background(0)
    # Optional: adjust noise detail here
    # noiseDetail(8, 0.65) # https://processing.org/reference/noiseDetail_.html
    global zoff #, step, zstep
    
    loadPixels()
    
    xoff = 0.0 # Start xoff at 0
    # For every x,y coordinate in a 2D space, calculate a noise value and produce a brightness value
    for x in range(width):
        xoff += step # Increment xoff
        yoff = 0.0   # For every xoff, start yoff at 0
        for y in range(height):
            yoff += step # Increment yoff
            
            # Calculate noise and scale by 255
            bright = noise(xoff, yoff,zoff) * 255
            
            # Try using this line instead
            # bright = random(0,255)
            
            # Set each pixel onscreen to a grayscale value
            pixels[x + y * width] = color(bright, bright, bright)
            
    updatePixels()
    
    zoff += zstep # Increment zoff 