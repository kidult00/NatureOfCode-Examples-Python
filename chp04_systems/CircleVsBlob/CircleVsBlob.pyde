# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(200, 200)
    background(0)

    img = loadImage("texture.png")
    image(img, 0, 0, width, height)
    save("blob.tif")

    fill(255)
    noStroke()
    ellipse(100, 100, width, height)
    save("circle.tif")

def draw():
    pass
